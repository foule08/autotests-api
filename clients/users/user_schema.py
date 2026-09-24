from pydantic import BaseModel, Field, ConfigDict
from pydantic import EmailStr


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
    email: EmailStr
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class UserSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class UpdateUserRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class GetUserResponseSchema(BaseModel):
    user: UserSchema

class CreateUserResponseSchema(BaseModel):
    user: UserSchema