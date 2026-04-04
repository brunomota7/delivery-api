from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from models import User
from dependencies import get_session
from main import bcrypt_context
from sqlalchemy.orm import Session
from schemas import CreateUserSchema

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/register")
async def register_user(user_schema: CreateUserSchema, session: Session = Depends(get_session)):
    user = session.query(User).filter(User.email == user_schema.email).first()

    if user:
        raise HTTPException(status_code=400, detail="User whit this email already exists")
    else:
        password_hash = bcrypt_context.hash(user_schema.password)
        new_user = User(user_schema.name, user_schema.email, password_hash, user_schema.admin)
        session.add(new_user)
        session.commit()
        return JSONResponse(status_code=201, content={"message": "User created successfully"})