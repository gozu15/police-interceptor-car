from fastapi import APIRouter

from src.database import SessionDB
from src.schemas.person import PersonCreate, PersonUpdate
import src.controllers.person_controller as PersonController


router = APIRouter()


@router.get("/", name="Get all persons")
def getAll(db: SessionDB):
  return PersonController.getAll(db)


@router.get("/{id}", name="Get a person by id")
def getOne(db: SessionDB, id: int):
  return PersonController.getOne(db, id)


@router.post("/person", name="Create a new person")
def create(db: SessionDB, data: PersonCreate):
  return PersonController.create(db, data)


@router.patch("/{id}", name="Update a person")
def update(db: SessionDB, id: int, input: PersonUpdate):
  return PersonController.update(db, id, input)


@router.delete("/{id}", name="Delete a person")
def delete(db: SessionDB, id: int):
  return PersonController.delete(db, id)
