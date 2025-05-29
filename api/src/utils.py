import jwt
from datetime import datetime, timedelta

from src.config import config


def verify_password(plain_password: str, hashed_password: str) -> bool:
  from passlib.context import CryptContext

  pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
  return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
  from passlib.context import CryptContext

  pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
  return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
  to_encode = data.copy()
  expire = datetime.utcnow() + (
    expires_delta if expires_delta else timedelta(minutes=config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
  )
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, config.JWT_SECRET_KEY, algorithm=config.JWT_ALGORITHM)
  return encoded_jwt


def decode_access_token(token: str) -> dict:
  try:
    payload = jwt.decode(token, config.JWT_SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
    return payload
  except jwt.JWTError:
    return None
