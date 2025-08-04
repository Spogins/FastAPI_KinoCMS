# -*- coding: utf-8 -*-
"""
Settings package.
"""
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings API.
    """

    PROJECT_NAME: str = "FastAPI_KinoCMS"
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    @property
    def DATABASE_URL(self) -> str:
        """
        Return async SQLAlchemy database URL for asyncpg driver.
        """
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}"  # noqa: E231
            f":{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}"  # noqa: E231
            f":{self.POSTGRES_PORT}/{self.POSTGRES_DB}"  # noqa: E231
        )

    @property
    def SYNC_DATABASE_URL(self) -> str:
        """
        Return sync SQLAlchemy database URL for alembic migrations.
        """
        return (
            f"postgresql://{self.POSTGRES_USER}"  # noqa: E231
            f":{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}"  # noqa: E231
            f":{self.POSTGRES_PORT}/{self.POSTGRES_DB}"  # noqa: E231
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """
    Get settings.
    """
    return Settings()


settings = get_settings()
