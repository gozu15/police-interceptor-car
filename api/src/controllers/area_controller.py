from fastapi import HTTPException
from sqlmodel import select

from src.db.database import SessionDB
from src.db.schemas import Area
from src.models.area import AreaCreate, AreaUpdate


def getAll(db: SessionDB) -> list[Area]:
  db_areas = db.exec(select(Area).offset(0).limit(100)).all()
  return db_areas


def getOne(id: int, db: SessionDB) -> Area:
  db_area = db.exec(select(Area).where(Area.id == id)).first()

  if db_area is None:
    raise HTTPException(status_code=404, detail="Area not found")
  else:
    return db_area


def create(input: AreaCreate, db: SessionDB) -> Area:
  db_area = db.exec(select(Area).where(Area.code == input.code)).first()

  print("hola pase")

  if db_area is not None:
    raise HTTPException(status_code=400, detail="Code already exists")

  new_area = Area(**input.model_dump())

  db.add(new_area)
  db.commit()
  db.refresh(new_area)

  return new_area


def update(id: int, input: AreaUpdate, db: SessionDB) -> AreaUpdate:
  db_area = db.exec(select(Area).where(Area.id == id)).first()

  if db_area is None:
    raise HTTPException(status_code=404, detail="Area not found")
  else:
    person_data = input.model_dump(exclude_unset=True)

    for key, value in person_data.items():
      setattr(db_area, key, value)

    db.add(db_area)
    db.commit()
    db.refresh(db_area)
    return db_area


def delete(id: int, db: SessionDB) -> bool:
  db_area = db.exec(select(Area).where(Area.id == id)).first()

  if db_area is None:
    raise HTTPException(status_code=404, detail="Area not found")
  else:
    db.delete(db_area)
    db.commit()
    return True
