from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import jwt
import toml 

with open('app/core/config.toml', 'r') as file:
    config_data = toml.load(file)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    # JSON Web Token (JWT) to encrypt JSON data during transfers
    encoded_jwt = jwt.encode(to_encode, config_data[auth].secret_key, algorithm=config_data[auth].algorithm)
    return encoded_jwt
