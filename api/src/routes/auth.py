from fastapi import APIRouter

from src.schemas.auth import UserLogin
from src.database import SessionDB

import src.controllers.auth_controller as AuthController


router = APIRouter()


@router.post("/login", name="Login with username and password")
def login(
  db: SessionDB,
  data: UserLogin,
):
  return AuthController.login(db, data)
