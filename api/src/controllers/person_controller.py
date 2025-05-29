from fastapi import HTTPException
from sqlmodel import select

from src.database import SessionDB
from src.models.person import Person
from src.schemas.person import PersonCreate, PersonUpdate


def getAll(db: SessionDB, offset: int = 0, limit: int = 100) -> list[Person]:
  db_users = db.exec(select(Person).offset(offset).limit(limit)).all()
  return db_users


def getOne(db: SessionDB, id: int) -> Person:
  db_person = db.exec(select(Person).where(Person.id == id)).first()

  if db_person is None:
    raise HTTPException(status_code=404, detail="Person not found")
  else:
    return db_person


def create(
  db: SessionDB,
  input: PersonCreate,
):
  db_person = db.exec(select(Person).where(Person.identification_number == input.identification_number)).first()

  if db_person is not None:
    raise HTTPException(status_code=400, detail="Identification number already exists")

  db_person = db.exec(select(Person).where(Person.email == input.email)).first()
  if db_person:
    raise HTTPException(status_code=400, detail="Email already exists")

  new_person = Person(**input.model_dump())

  db.add(new_person)
  db.commit()
  db.refresh(new_person)

  return new_person


def update(
  db: SessionDB,
  id: int,
  input: PersonUpdate,
) -> Person:
  db_person = db.exec(select(Person).where(Person.id == id)).first()

  if db_person is None:
    raise HTTPException(status_code=404, detail="Person not found")
  else:
    person_data = input.model_dump(exclude_unset=True)

    print(person_data)

    for key, value in person_data.items():
      setattr(db_person, key, value)

    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


def delete(db: SessionDB, id: int) -> bool:
  db_person = db.exec(select(Person).where(Person.id == id)).first()

  if db_person is None:
    raise HTTPException(status_code=404, detail="Person not found")
  else:
    db.delete(db_person)
    db.commit()
    return True
