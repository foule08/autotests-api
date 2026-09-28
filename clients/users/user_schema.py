from pydantic import BaseModel, Field, ConfigDict
from pydantic import EmailStr

from tools.fakers import fake


class CreateUserRequestSchema(BaseModel):
    """
    Структура данных для создания пользователя.

    Attributes:
        email: Электронная почта пользователя.
        password: Пароль пользователя.
        lastName: Фамилия пользователя.
        firstName: Имя пользователя.
        middleName: Отчество пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)
    email: EmailStr = Field(default_factory = fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias='lastName', default_factory=fake.last_name)
    first_name: str = Field(alias='firstName', default_factory=fake.first_name)
    middle_name: str = Field(alias='middleName', default_factory=fake.middle_name)

class UserSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class UpdateUserRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    email: EmailStr = Field(default_factory=fake.email)
    last_name: str = Field(alias='lastName', default_factory=fake.last_name)
    first_name: str = Field(alias='firstName', default_factory=fake.first_name)
    middle_name: str = Field(alias='middleName', default_factory=fake.middle_name)

class GetUserResponseSchema(BaseModel):
    user: UserSchema

class CreateUserResponseSchema(BaseModel):
    user: UserSchema