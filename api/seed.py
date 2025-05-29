from sqlmodel import Session, select
from passlib.context import CryptContext

from src.core.database import engine, create_db_and_tables
from src.models.user import User
from src.models.enums import Gender


def seed_admin_user():
  pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

  user = User(
    identification_number="123456789",
    name="Super",
    last_name="Admin",
    gender=Gender.male,
    email="superadmin@yopmail.com",
    username="root",
    password=pwd_context.hash("root"),
  )

  data = User.model_validate(user)

  with Session(engine) as session:
    existing_admin = session.exec(select(User).where(User.username == data.username)).first()

    if not existing_admin:
      session.add(data)
      session.commit()
      print("Admin user created")
    else:
      print("Admin user already exists")


if __name__ == "__main__":
  create_db_and_tables()
  seed_admin_user()
