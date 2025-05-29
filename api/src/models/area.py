from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Area(BaseModel):
  id: int
  code: str
  name: str
  description: Optional[str] = None
  created_at: datetime
  updated_at: datetime


class AreaCreate(BaseModel):
  code: str
  name: str
  description: Optional[str] = None


class AreaUpdate(BaseModel):
  code: Optional[str] = None
  name: Optional[str] = None
  description: Optional[str] = None
