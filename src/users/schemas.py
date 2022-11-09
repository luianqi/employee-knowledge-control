from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr


class Roles(Enum):
    user = "user"
    owner = "owner"
    admin = "admin"


class UserBase(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    role: Roles = "user"
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True


class UserSignUp(UserBase):
    password: str


class UserSignIn(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[Roles] = None
    is_active: Optional[bool] = True


class UpdatePassword(BaseModel):
    current_password: Optional[str] = None
    new_password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr


class TokenData(BaseModel):
    email: Optional[str] = None



