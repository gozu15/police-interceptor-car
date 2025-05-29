import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = ROOT_DIR / ".env"

print(ROOT_DIR)

load_dotenv(dotenv_path=ENV_PATH)


class Config(BaseSettings):
  ENVIROMENT: str = os.getenv("ENVIROMENT", "development")
  APP_PORT: int = os.getenv("APP_PORT", 8000)

  DB_USER: str = os.getenv("DB_USER")
  DB_PASSWORD: str = os.getenv("DB_PASSWORD")
  DB_HOST: str = os.getenv("DB_HOST", "localhost:3306")
  DB_NAME: str = os.getenv("DB_NAME")

  JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
  JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")
  JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES")


config = Config()
