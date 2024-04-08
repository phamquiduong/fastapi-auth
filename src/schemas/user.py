from pydantic import BaseModel, EmailStr

from schemas import Group


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserLogin(UserBase):
    password: str


class User(UserBase):
    id: int
    group: Group | None = None

    class Config:
        from_attributes = True
