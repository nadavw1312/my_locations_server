from dotenv import load_dotenv
import os

from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = os.environ['JWT_SECRET_KEY']
    JWT_REFRESH_SECRET_KEY: str = os.environ['JWT_REFRESH_SECRET_KEY']
    ALGORITHM: str = os.environ['ALGORITHM']
    DB_USER: str = os.environ['DB_USER']
    DB_PASS: str = os.environ['DB_PASS']
    DB_IP: str = os.environ['DB_IP']
    DB_NAME: str = os.environ['DB_NAME']
    

    class Config:
        case_sensitive = True


settings = Settings()
