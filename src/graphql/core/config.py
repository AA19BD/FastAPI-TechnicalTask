import os

from pydantic import BaseSettings
from dotenv import load_dotenv
from pathlib import Path


env_path = Path(".") / "envs/.env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    HOST_PORT: str = os.getenv("HOST_PORT")
    HOST_URL: str = os.getenv("HOST_URL")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", 5432))
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
