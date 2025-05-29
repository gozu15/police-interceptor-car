from fastapi import HTTPException, status, Request
from sqlmodel import select
from jwt import PyJWTError

from src.db.database import SessionDB
from src.db.schemas import User as UserSchema
from src.core.utils import decode_access_token
from src.models.auth import User


async def get_current_user(request: Request, db: SessionDB) -> User:
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
    payload = decode_access_token(token)
    username: int = payload.get("sub")

    if username is None:
      raise credentials_exception
  except PyJWTError:
    raise credentials_exception

  user = db.exec(select(UserSchema).where(UserSchema.username == username)).first()
  if user is None:
    raise credentials_exception

  return user
