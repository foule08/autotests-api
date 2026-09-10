from httpx import Response
from typing import TypedDict
from clients.api_client import ApiClient


class CreateUserRequest(TypedDict):
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


class PublicUsersClient(ApiClient):
    """
    API клиент для работы с публичными методами эндпоинта /api/v1/users.

    Содержит методы, не требующие авторизации, такие как создание пользователя.
    """

    def create_user_api(self, request: CreateUserRequest) -> Response:
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

        Example:
            >>> client = PublicUsersClient(http_client)
            >>> response = client.create_user_api({
            ...     "email": "user@example.com",
            ...     "password": "secret123",
            ...     "lastName": "Ivanov",
            ...     "firstName": "Ivan",
            ...     "middleName": "Ivanovich"
            ... })
            >>> print(response.status_code)
            201
        """
        return self.post("/api/v1/users", json=request)