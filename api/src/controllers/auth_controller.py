from fastapi import HTTPException
from sqlmodel import select
from datetime import timedelta

from src.config import config
from src.database import SessionDB
from src.models.user import User
from src.schemas.auth import UserLogin
from src.utils import create_access_token, verify_password


def login(
  db: SessionDB,
  input: UserLogin,
):
  db_user = db.exec(select(User).where(User.username == "root")).first()

  if db_user is None:
    raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
  else:
    pwd_valid = verify_password(input.password, db_user.password)

    if pwd_valid is False:
      raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")

    access_token_expires = timedelta(minutes=config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": db_user.username}, expires_delta=access_token_expires)

    return {
      "id": db_user.id,
      "name": db_user.name,
      "last_name": db_user.last_name,
      "access_token": access_token,
    }
