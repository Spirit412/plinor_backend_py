from api import crud
from api.database.sqlalchemy_connection import get_session, get_session_stub
from api.factories.user import user_factory
from api.routers.market_routers.marketplace_routs import marketplace_router
from api.routers.v1_routers.client.client import client_router
from api.routers.v1_routers.dictionaries.new_dictionaries import \
    dictionaries_router
from api.routers.v1_routers.new_address import address_router
from api.routers.v1_routers.new_good import good_router
from api.routers.v1_routers.new_good_category import good_category_router
from api.routers.v1_routers.new_organization import organization_router
from api.routers.v1_routers.new_roles import roles_router
from api.routers.v1_routers.new_sales_point import sales_point_router
from api.routers.v1_routers.new_user import user_router
from api.routers.v1_routers.new_user_roles import user_roles_router
from api.routers.v1_routers.notifications import notifications_router
# from api.celery_email_tasks import EmailTasks
import api.celery_email_tasks as EmailTasks
from api.routers.v1_routers.outside_organization import \
    outside_organization_router
from api.routers.v1_routers.outside_organization_partnership import \
    outside_partnership_router
from api.routers.v1_routers.posts_feed import posts_feed_router
from api.routers.v1_routers.supplier.supplier import supplier_router
from api.routers.v1_routers.system.system import system_router
from api.routers.v1_routers.stocktaking_docs import stocktaking_docs_router
from api.routers.v1_routers.expense_category import expense_category_router
from api.routers.v1_routers.expense_docs import expense_docs_router
from api.routers.v1_routers.write_off_docs import write_off_router
from api.routers.v1_routers.write_off_docs_items import write_off_items_router
from api.routers.v1_routers.write_off_reason import write_off_reason_router
from api.routers.v1_routers.custom_properties import custom_properties_router
from api.routers.v1_routers.custom_properties_remembership import custom_properties_remembership_router
from api.schemas.token import Token
from api.schemas.user import UserCreate
from fastapi import APIRouter, Depends, Request, Response
from fastapi.routing import APIRoute
from sqlalchemy.orm import Session
from asyncio.log import logger

v1_router = APIRouter(
    prefix='/v1',
    tags=[],
    dependencies=[],
    responses={404: {'description': 'Not found'}},
    # route_class=ContextIncludedRoute,
)

v1_router.include_router(user_router,
                         prefix="/users", tags=[TagsRu.USERS])


@v1_router.post('/signup')
@v1_router.post('/signup/',
                include_in_schema=False)
async def signup(user: UserCreate,
                 session: Session = Depends(get_session_stub),
                 ) -> Token:
    access_token = user_factory.create_user_no_commit(session=session, user=user)
    # email_service = crud.EmailService()

    try:
        task = EmailTasks.send_welcome_mail.delay(email_to=user.email,
                                                  subject="Добро пожаловать!",
                                                  head="Добро пожаловать на Маркет!",
                                                  foot="Если вы не регистрировались, просто проигнорируйте это письмо.",
                                                  )
        logger.info(msg=f"Task run: {task}")
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        logger.warning(msg=f"Ошибка постановки задачи в Celery. detail: {e}")
        return False

    # if email_service.send_welcome_mail(email=user.email):
    #     return {"access_token": access_token, "token_type": "bearer"}
    # else:
    #     return False