from __future__ import annotations


from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.dialects.postgresql import JSONB
from base_model import BaseModel
from typing import Optional

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class User(SQLAlchemyBaseUserTable[int], BaseModel):
    __tablename__: str = "user"

    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    middle_name: Mapped[str] = mapped_column(String(length=1024), nullable=True)
    last_name: Mapped[str] = mapped_column(String(length=1024), nullable=True)
    phone: Mapped[str] = mapped_column(String(length=30), nullable=True)
    properties_config: Mapped[Optional[dict]] = mapped_column(JSONB, default={}, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
