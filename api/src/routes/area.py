from fastapi import APIRouter, Depends, Security
from fastapi.security import HTTPBearer

from src.db.database import SessionDB
from src.core.helper import get_current_user
from src.models.area import Area, AreaCreate, AreaUpdate
import src.controllers.area_controller as AreaController

bearer_scheme = HTTPBearer()
router = APIRouter(
  dependencies=[Security(bearer_scheme), Depends(get_current_user)],
)


@router.get("/", name="Get all areas", response_model=list[Area])
def getAll(db: SessionDB):
  return AreaController.getAll(db)


@router.get("/{id}", name="Get a area by id", response_model=Area)
def getOne(id: int, db: SessionDB):
  return AreaController.getOne(id, db)


@router.post("/person", name="Create a new area", response_model=Area)
def create(data: AreaCreate, db: SessionDB):
  return AreaController.create(data, db)


@router.patch("/{id}", name="Update a area", response_model=AreaUpdate)
def update(id: int, input: AreaUpdate, db: SessionDB):
  return AreaController.update(id, input, db)


@router.delete("/{id}", name="Delete a area", response_model=bool)
def delete(id: int, db: SessionDB):
  return AreaController.delete(id, db)
