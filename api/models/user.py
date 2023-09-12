from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import JSONB
from base_model import BaseModel
from typing import Optional

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import Select


class User(SQLAlchemyBaseUserTable[int], BaseModel):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    middle_name: Mapped[str] = mapped_column(String(length=1024), nullable=True)
    last_name: Mapped[str] = mapped_column(String(length=1024), nullable=True)
    phone: Mapped[str] = mapped_column(String(length=1024), nullable=True)
    preferences: Mapped[Optional[dict]] = mapped_column(JSONB, default={}, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
