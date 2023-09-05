from asyncio.log import logger

from fastapi import APIRouter
# from fastapi.routing import APIRoute
from .user import user_router

v1_router = APIRouter(
    prefix="/v1",
    tags=[],
    dependencies=[],
    responses={404: {"description": "Not found"}},
    # route_class=ContextIncludedRoute,
)

v1_router.include_router(user_router,
                         prefix="/users", tags=["USERS"])


@v1_router.post("/signup")
@v1_router.post("/signup/", include_in_schema=False)
async def signup():
    """Регистрация

    Returns:
        Token: _description_
    """
    NotImplemented
