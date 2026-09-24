from httpx import Response
from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(ApiClient):
    """
    API клиент для работы с публичными методами эндпоинта /api/v1/users.

    Содержит методы, не требующие авторизации, такие как создание пользователя.
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
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
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_public_users_client():
    return PublicUsersClient(client=get_public_http_client())