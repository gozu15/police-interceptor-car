from pydantic import BaseModel
from datetime import datetime


class Area(BaseModel):
  id: int
  code: str
  name: str
  description: str | None = None
  created_at: datetime
  updated_at: datetime


class AreaCreate(BaseModel):
  code: str
  name: str
  description: str | None = None


class AreaUpdate(BaseModel):
  code: str | None = None
  name: str | None = None
  description: str | None = None
