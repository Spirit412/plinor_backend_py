from __future__ import annotations

import contextlib
from asyncio.log import logger
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from api.database.async_session import AsyncSessionManager
from api.utils import timeit


async def get_async_session_stub():
    raise NotImplementedError  # это реально тело этой функции

# Dependency
# @contextlib.asynccontextmanager


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


class TX(AsyncSession):
    def __new__(cls, db: AsyncSession = Depends(get_async_session)):
        return db


Base: DeclarativeMeta = declarative_base()


__all__ = ["Base", "get_async_session", "TX"]