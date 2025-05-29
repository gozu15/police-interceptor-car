from fastapi import HTTPException, status, Request
from sqlmodel import select
from jwt import PyJWTError, decode as jwt_decode

from src.core.database import SessionDB
from src.core.config import config
from src.schemas.user import User


async def get_current_user(request: Request, db: SessionDB):
  authorization: str | None = request.headers.get("Authorization")
  if not authorization:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="No authentication token provided",
      headers={"WWW-Authenticate": "Bearer"},
    )

  token = authorization.split(" ")[1]
  if not token:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid authentication token format",
      headers={"WWW-Authenticate": "Bearer"},
    )

  credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid token",
    headers={"WWW-Authenticate": "Bearer"},
  )

  try:
    payload = jwt_decode(token, config.JWT_SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
    username: int = payload.get("sub")

    if username is None:
      raise credentials_exception
  except PyJWTError:
    raise credentials_exception

  user = db.exec(select(User).where(User.username == username)).first()
  if user is None:
    raise credentials_exception

  return user
