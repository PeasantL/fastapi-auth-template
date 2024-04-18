from sqlalchemy.orm import Session
from ..core.security import verify_password
from .crud_user import get_user_by_username


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):  
        return False
    return user
