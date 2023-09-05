from fastapi import APIRouter, Depends, Query
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession
from api.database.decorators import managed_transaction
from api import crud, schemas
from api.database.sqlalchemy_connection import get_async_session_stub
from api.factories.user import AsyncUserFactoryToUpdate
from api.responses import exceptions


user_router = APIRouter(
    prefix="",
    tags=[],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@user_router.post("/login")
@user_router.post("/login/", include_in_schema=False)
async def user_login_for_access_token():

    """ 
    **Получить токен по EMAIL и паролю.**
    В поле `username` - необходимо ввести email.
    """
    
    NotImplemented


@user_router.get("/me")
@user_router.get("/me/",  include_in_schema=False)
async def user_get_me():

    """
    **Получить данные текущего юзера.**
    """
    
    NotImplemented


@user_router.get("/forgot_password")
@user_router.get("/forgot_password/", include_in_schema=False)
async def user_reset_password():

    """
    **Отослать на почту токен, для восстановления пароля.**
    """
    
    NotImplemented


##########

@user_router.get("/change_password")
@user_router.get("/change_password/", include_in_schema=False)
async def user_change_password():

    """
    **Изменить пароль с помощью токена восстановления. Получить его можно по forgot_password**
    """
    
    NotImplemented


@user_router.get("/verify_email")
@user_router.get("/verify_email/", include_in_schema=False)
async def user_verify_organization_email():

    """
    **Верифицировать email.**
    Время "жизни" токена с момента создания = ХХ минут
    """
    
    NotImplemented


@user_router.get("/init_verify_email")
@user_router.get("/init_verify_email/", include_in_schema=False)
async def user_email_verification():

    """
    **Отправить письмо подтверждения на почту.**
    """
    
    NotImplemented


@user_router.put("")
@user_router.put("/", include_in_schema=False)
async def update_user() -> schemas.UserBase:

    """
    **Изменить имя, телефон или email пользователя.**
    """
    
    NotImplemented