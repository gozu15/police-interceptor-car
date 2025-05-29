from pydantic import BaseModel
from datetime import date, datetime

from src.db.schemas import Gender, Type


class Person(BaseModel):
  id: int
  photo: str | None = None
  identification_number: str
  name: str
  last_name: str
  gender: Gender
  birthdate: date
  type: Type
  email: str
  created_at: datetime
  updated_at: datetime


class PersonCreate(BaseModel):
  photo: str | None = None
  identification_number: str
  name: str
  last_name: str
  gender: Gender
  birthdate: date
  type: Type
  email: str


class PersonUpdate(BaseModel):
  photo: str | None = None
  identification_number: str | None = None
  name: str | None = None
  last_name: str | None = None
  gender: Gender | None = None
  birthdate: date | None = None
  type: Type | None = None
  email: str | None = None
