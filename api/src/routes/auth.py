from fastapi import APIRouter, Depends, Security
from fastapi.security import HTTPBearer
from typing import Annotated

from src.core.database import SessionDB
from src.core.helper import get_current_user
from src.schemas.user import User
from src.models.auth import UserLogin, AuthResponse
import src.controllers.auth_controller as AuthController

bearer_scheme = HTTPBearer()
router = APIRouter()


@router.post("/login", name="Login with username and password", response_model=AuthResponse)
def login(
  data: UserLogin,
  db: SessionDB,
):
  return AuthController.login(data, db)


@router.post("/get_current_user", name="Get current user", response_model=User, dependencies=[Security(bearer_scheme)])
async def get_current_user(
  current_user: Annotated[User, Depends(get_current_user)],
):
  return current_user
