from fastapi import HTTPException
from sqlmodel import select

from src.core.database import SessionDB
from src.schemas.person import Person
from src.models.person import PersonCreate, PersonUpdate


def getAll(db: SessionDB) -> list[Person]:
  db_users = db.exec(select(Person).offset(0).limit(100)).all()
  return db_users


def getOne(id: int, db: SessionDB) -> Person:
  db_person = db.exec(select(Person).where(Person.id == id)).first()

  if db_person is None:
    raise HTTPException(status_code=404, detail="Person not found")
  else:
    return db_person


def create(input: PersonCreate, db: SessionDB) -> Person:
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


def update(id: int, input: PersonUpdate, db: SessionDB) -> Person:
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


def delete(id: int, db: SessionDB) -> bool:
  db_person = db.exec(select(Person).where(Person.id == id)).first()

  if db_person is None:
    raise HTTPException(status_code=404, detail="Person not found")
  else:
    db.delete(db_person)
    db.commit()
    return True
