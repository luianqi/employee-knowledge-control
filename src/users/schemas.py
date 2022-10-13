from typing import Optional, List

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
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
    is_active: Optional[bool] = True


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class UsersList(BaseModel):
    id: int
    users: List[UserBase]

    class Config:
        orm_mode = True
