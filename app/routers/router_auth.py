from datetime import timedelta
from typing import Annotated
import toml

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from ..core.security import create_access_token
from ..core.database import SessionLocal
from ..crud.crud_auth import authenticate_user
from ..schemas.schema_token import Token


with open('app/core/config.toml', 'r') as file:
    config_data = toml.load(file)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=config_data[auth].access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")