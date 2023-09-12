from typing import NoReturn
from fastapi import HTTPException, status


async def raise_logic_exception(message: str) -> NoReturn:
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=message,
        headers={"WWW-Authenticate": "Bearer"}
    )


def raise_validation_error(field: str) -> NoReturn:
    """Поле {field} не прошло валидацию."""
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"Поле {field} не прошло валидацию.",
        headers={"WWW-Authenticate": "Bearer"},
    )