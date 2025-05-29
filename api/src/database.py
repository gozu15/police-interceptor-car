from typing import Annotated
from fastapi import Depends
from sqlmodel import create_engine, Session, SQLModel

from src.config import config


DATABASE_URL = f"mysql+pymysql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False)


def create_db_and_tables():
  SQLModel.metadata.create_all(engine)


def get_session():
  with Session(engine) as session:
    yield session


SessionDB = Annotated[Session, Depends(get_session)]
