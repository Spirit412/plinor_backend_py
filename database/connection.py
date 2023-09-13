from __future__ import annotations

from asyncio.log import logger
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base
from database.session import AsyncSessionManager
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import registry


async def get_session_stub():
    raise NotImplementedError  # это реально тело этой функции


async def get_session() -> AsyncSession:
    SessionLocal: AsyncSession = AsyncSessionManager().AsyncSessionLocal
    async with SessionLocal() as session:
        try:
            yield session
        except (Exception, HTTPException) as e:
            logger.error(e)
            await session.rollback()
            raise
        else:
            await session.commit()
        finally:
            await session.close()



mapper_registry = registry()

Base = mapper_registry.generate_base()


__all__ = ["Base", "get_session", "get_session_stub"]
