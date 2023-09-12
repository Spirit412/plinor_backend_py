from __future__ import annotations
from asyncio.log import logger
from datetime import datetime
from typing import NoReturn
import phonenumbers
from phonenumbers import NumberParseException
from pydantic import BaseModel, root_validator, Field, EmailStr
from api.responses.exceptions import raise_logic_exception, raise_validation_error
from api.schemas.user_access_controls import UserAccessControls
from api import schemas
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: EmailStr
    hashed_password: str
    name: str | None = None
    middle_name: str | None = None
    last_name: str | None = None
    phone: str | None = None
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserCreate(UserBase):
    email: EmailStr
    password: str

    @root_validator
    def validate_fields(cls, values):

        if values.get('phone') is None or "":
            values['phone'] = None
        else:
            try:
                phone_parse = phonenumbers.parse(
                    values.get('phone'), region='RU')
            except NumberParseException as e:
                raise_logic_exception(
                    message=f'Поле phone = {values.get("phone")} не прошло валидацию.')
            values['phone'] = str(phone_parse.country_code) + \
                str(phone_parse.national_number)
        return values


class UserDB(UserBase):

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None

    class Config:
        orm_mode = True
