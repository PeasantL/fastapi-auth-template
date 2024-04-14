from pydantic import BaseModel
from typing import Optional

from .schema_item import Item


class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        from_attributes = True

class UserUpdate(UserBase):
    username: Optional[str] = None
    is_active: Optional[bool] = None
    password: Optional[str] = None