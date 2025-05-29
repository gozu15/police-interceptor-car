from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import func
from datetime import date, datetime, timezone
from enum import Enum


class Gender(str, Enum):
  male = "male"
  female = "female"
  other = "other"


class Type(str, Enum):
  student = "student"
  master = "master"


class DayOfWeek(str, Enum):
  Monday = "Monday"
  Tuesday = "Tuesday"
  Wednesday = "Wednesday"
  Thursday = "Thursday"
  Friday = "Friday"
  Saturday = "Saturday"
  Sunday = "Sunday"


class User(SQLModel, table=True):
  __tablename__ = "users"

  id: int | None = Field(default=None, primary_key=True)

  photo: str | None = Field(default=None)
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


class Person(SQLModel, table=True):
  __tablename__ = "persons"

  id: int | None = Field(default=None, primary_key=True)

  photo: str | None = Field(default=None)
  identification_number: str = Field(unique=True)
  name: str = Field()
  last_name: str = Field()
  gender: Gender = Field()
  birthdate: date = Field()
  type: Type = Field()
  email: str = Field(index=True, unique=True)

  created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
  updated_at: datetime = Field(
    default_factory=lambda: datetime.now(timezone.utc), nullable=False, sa_column_kwargs={"onupdate": func.now()}
  )


class Area(SQLModel, table=True):
  __tablename__ = "areas"

  id: int | None = Field(default=None, primary_key=True)

  code: str = Field(unique=True, index=True)
  name: str = Field()
  description: str | None = Field(default=None)

  created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
  updated_at: datetime = Field(
    default_factory=lambda: datetime.now(timezone.utc), nullable=False, sa_column_kwargs={"onupdate": func.now()}
  )

  # schedules: list["Schedule"] = Relationship(back_populates="area")


class Schedule(SQLModel, table=True):
  __tablename__ = "schedules"

  id: int | None = Field(default=None, primary_key=True)
  name: str = Field()
  description: int | None = Field(default=None)
  start_time: datetime = Field()
  end_time: datetime = Field()

  created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
  updated_at: datetime = Field(
    default_factory=lambda: datetime.now(timezone.utc), nullable=False, sa_column_kwargs={"onupdate": func.now()}
  )

  # area_id: int | None = Field(default=None, foreign_key="area.id")
  # area: Area | None = Relationship(back_populates="schedules")
