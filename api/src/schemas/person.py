from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from src.models.enums import Gender, Type


class PersonCreate(BaseModel):
  photo: Optional[str] = None
  identification_number: str
  name: str
  last_name: str
  gender: Gender
  birthdate: datetime
  type: Type
  email: str


class PersonUpdate(BaseModel):
  photo: Optional[str] = None
  identification_number: Optional[str] = None
  name: Optional[str] = None
  last_name: Optional[str] = None
  gender: Optional[Gender] = None
  birthdate: Optional[datetime] = None
  type: Optional[Type] = None
  email: Optional[str] = None
