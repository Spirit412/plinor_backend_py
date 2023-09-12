from __future__ import annotations

from asyncio.log import logger
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from database.async_session import AsyncSessionManager


async def get_async_session_stub():
    raise NotImplementedError  # это реально тело этой функции


async def get_async_session() -> AsyncSession:
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


Base: DeclarativeMeta = declarative_base()

__all__ = ["Base", "get_async_session"]