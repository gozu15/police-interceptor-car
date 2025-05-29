from sqlmodel import SQLModel, Field
from sqlalchemy import func
from typing import Optional
from datetime import datetime, timezone

from src.models.enums import Gender


class User(SQLModel, table=True):
  __tablename__ = "users"

  id: Optional[int] = Field(default=None, primary_key=True)

  photo: Optional[str] = Field(default=None)
  identification_number: str = Field(unique=True)
  name: str = Field()
  last_name: str = Field()
  gender: Gender = Field()
  email: str = Field(index=True, unique=True)
  username: str = Field(index=True, unique=True)
  password: str = Field()

  created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
  updated_at: datetime = Field(
    default_factory=lambda: datetime.now(timezone.utc), nullable=False, sa_column_kwargs={"onupdate": func.now()}
  )
