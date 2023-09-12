from pydantic import Field
from functools import lru_cache
from pathlib import Path
from enum import Enum
from pydantic_settings import BaseSettings

class Environment(str, Enum):
    LOCAL = "LOCAL"
    DEMO = "DEMO"
    PRODUCTION = "PRODUCTION"
    DEVELOPMENT = "DEVELOPMENT"
    STAGING = "STAGING"


class Settings(BaseSettings):

    BASE_URL: str | None = Field(None)
    ENVIRONMENT: Environment | None = Field(Environment.DEVELOPMENT)
    APP_PORT: str | int
    PROJECT_NAME: str
    RADIS_PORT: str | int

    SECRET_KEY: str | None = Field(None)
    ALGORITHM: str | None = Field(None)

    DB_HOST: str | None = Field(None)
    DB_PROTOCOL: str | None = Field("postgresql")
    DB_DRIVER: str | None = Field("asyncpg")
    DB_DBNAME: str | None = Field(None)
    DB_PORT: str | None = Field(None)
    DB_USER: str | None = Field(None)
    DB_PASSWORD: str | None = Field(None)
    APP_DEBUG: bool = True


    class Config:
        env_file = Path.cwd() / ".env"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
