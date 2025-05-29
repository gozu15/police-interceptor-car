from fastapi import APIRouter, Depends, Security
from fastapi.security import HTTPBearer

from src.db.database import SessionDB
from src.core.helper import get_current_user
from src.models.person import Person, PersonCreate, PersonUpdate
import src.controllers.person_controller as PersonController

bearer_scheme = HTTPBearer()
router = APIRouter(
  dependencies=[Security(bearer_scheme), Depends(get_current_user)],
)


@router.get("/", name="Get all persons", response_model=list[Person])
def getAll(db: SessionDB):
  return PersonController.getAll(db)


@router.get("/{id}", name="Get a person by id", response_model=Person)
def getOne(id: int, db: SessionDB):
  return PersonController.getOne(id, db)


@router.post("/person", name="Create a new person", response_model=Person)
def create(data: PersonCreate, db: SessionDB):
  return PersonController.create(data, db)


@router.patch("/{id}", name="Update a person", response_model=PersonUpdate)
def update(id: int, input: PersonUpdate, db: SessionDB):
  return PersonController.update(id, input, db)


@router.delete("/{id}", name="Delete a person", response_model=bool)
def delete(id: int, db: SessionDB):
  return PersonController.delete(id, db)
