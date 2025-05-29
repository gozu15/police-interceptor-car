from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from src.db.schemas import Gender


class UserLogin(BaseModel):
  username: str
  password: str


class AuthResponse(BaseModel):
  id: int
  name: str
  last_name: str
  access_token: str


class User(BaseModel):
  id: int
  photo: str | None = None
  identification_number: str
  name: str
  last_name: str
  gender: Gender
  email: str
  username: str
  password: str
  created_at: datetime
  updated_at: datetime
