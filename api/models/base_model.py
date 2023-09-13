from __future__ import annotations

from typing import Optional
from database.connection import Base
from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import func
from typing_extensions import Annotated

timestamp = Annotated[
    datetime,
    mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),
]
intpk = Annotated[int, mapped_column(primary_key=True)]


class BaseModel(Base):
    __abstract__ = True
    id: Mapped[intpk]

    deleted_at: Mapped[Optional[datetime]] = mapped_column(default=None)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
