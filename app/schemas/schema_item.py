from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class ItemUpdate(ItemBase):
    title: str
    description: str
    owner_id: int