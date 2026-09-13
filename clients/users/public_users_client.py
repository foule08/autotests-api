from httpx import Response
from typing import TypedDict
from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client


class CreateUserRequestDict(TypedDict):
    """
    Структура данных для создания пользователя.

    Attributes:
        email: Электронная почта пользователя.
        password: Пароль пользователя.
        lastName: Фамилия пользователя.
        firstName: Имя пользователя.
        middleName: Отчество пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class User(TypedDict):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    user: User



class PublicUsersClient(ApiClient):
    """
    API клиент для работы с публичными методами эндпоинта /api/v1/users.

    Содержит методы, не требующие авторизации, такие как создание пользователя.
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Создание нового пользователя через API.

        Выполняет POST-запрос к эндпоинту /api/v1/users для регистрации
        нового пользователя в системе.

        Args:
            request: Словарь с данными пользователя, содержащий:
                - email (str): Электронная почта
                - password (str): Пароль
                - lastName (str): Фамилия
                - firstName (str): Имя
                - middleName (str): Отчество

        Returns:
            Response: Объект ответа от сервера с информацией о созданном
                     пользователе или ошибке валидации.
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> Response:
        response = self.create_user_api(request)
        return response.json()

def get_public_users_client():
    return PublicUsersClient(client=get_public_http_client())