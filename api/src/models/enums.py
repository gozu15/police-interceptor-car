from enum import Enum


class Gender(str, Enum):
  male = "male"
  female = "female"
  other = "other"


class Type(str, Enum):
  student = "student"
  master = "master"
