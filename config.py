import os
from dotenv import load_dotenv
load_dotenv()
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    VERSION: str = os.getenv("VERSION")
    DEBUG: bool = os.getenv("DEBUG")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT")

    API_PREFIX: str = os.getenv("API_PREFIX")

    SECRET_KEY: str = os.getenv("SECRET_KEY")

    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()