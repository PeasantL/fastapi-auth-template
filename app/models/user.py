from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # Items associated with user are deleted upon termination of user
    # Items without a associated user are also deleted
    items = relationship("Item", back_populates="owner", cascade="all, delete, delete-orphan")