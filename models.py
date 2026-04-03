import uuid
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Boolean, Integer, Float, ForeignKey, DateTime, UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

db = create_engine("postgresql+psycopg2://postgres:admin@localhost:5432/delivery_db")
Base = declarative_base()

class User(Base):
    __tablename__ = "tb_users"

    id = Column("id", UUID(as_uuid=True), primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    enabled = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False)
    is_admin = Column(Boolean)

    def __init__(self, name, email, password, is_admin=False):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.password = password
        self.enabled = True
        self.created_at = datetime.now()
        self.is_admin = is_admin

class Order(Base):
    __tablename__ = "tb_orders"

    # STATUS_ORDERS = (
    #     ("PENDENTE", "Pendente"),
    #     ("CANCELADO", "Cancelado"),
    #     ("FINALIZADO", "Finalizado")
    # )

    id = Column("id", UUID(as_uuid=True), primary_key=True)
    status = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    user =  Column("user_id", UUID(as_uuid=True), ForeignKey("tb_users.id"))
    created_at = Column(DateTime, nullable=False)

    def __init__(self, user, status="PENDENTE", price=0.00):
        self.id = uuid.uuid4()
        self.status = status
        self.price = price
        self.user = user
        self.created_at = datetime.now()

class OrderItem(Base):
    __tablename__ = "tb_order_items"

    id = Column("id", UUID(as_uuid=True), primary_key=True)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    order = Column("order_id", UUID(as_uuid=True), ForeignKey("tb_orders.id"))

    def __init__(self, order, quantity=0, unit_price=0.00):
        self.id = uuid.uuid4()
        self.quantity = quantity
        self.unit_price = unit_price
        self.order = order