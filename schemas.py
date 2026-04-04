from pydantic import BaseModel
from typing import Optional

class CreateUserSchema(BaseModel):
    name: str
    email: str
    password: str
    admin: Optional[bool]

    class Confing:
        from_attributes = True