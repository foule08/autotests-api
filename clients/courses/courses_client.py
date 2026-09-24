from httpx import Response
from pydantic import BaseModel

from clients.api_client import ApiClient
from clients.courses.courses_schema import (
    CreateCourseRequestSchema,
    CreateCourseResponseSchema,
    GetCoursesQuerySchema,
    GetCourseResponseSchema,
    GetCourseResponseSchema,
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema,
)
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class CoursesClient(ApiClient):
    """
    API клиент для работы с эндпоинтом /api/v1/courses.

    Содержит методы для получения, создания, обновления и удаления курсов.
    Требует авторизации (валидный токен в заголовках HTTP-клиента).
    """

    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Получение списка курсов с фильтрацией.

        :param query: Pydantic-модель с параметрами фильтрации (например, userId).
        :return: Сырой ответ сервера (httpx.Response).
        """
        return self.client.get(
            "/api/v1/courses",
            params=query.model_dump(by_alias=True, exclude_none=True),
        )

    def get_courses(self, query: GetCoursesQuerySchema) -> GetCourseResponseSchema:
        """
        Получение списка курсов с парсингом ответа в Pydantic-модель.

        :param query: Pydantic-модель с параметрами фильтрации.
        :return: Распарсенный ответ в виде GetCoursesResponseSchema.
        """
        response = self.get_courses_api(query)
        response.raise_for_status()
        return GetCourseResponseSchema.model_validate_json(response.text)

    def get_course_api(self, course_id: str) -> Response:
        """
        Получение одного курса по его идентификатору.

        :param course_id: UUID курса.
        :return: Сырой ответ сервера (httpx.Response).
        """
        return self.client.get(f"/api/v1/courses/{course_id}")

    def get_course(self, course_id: str) -> GetCourseResponseSchema:
        """
        Получение одного курса с парсингом ответа.

        :param course_id: UUID курса.
        :return: Распарсенный ответ в виде GetCourseResponseSchema.
        """
        response = self.get_course_api(course_id)
        response.raise_for_status()
        return GetCourseResponseSchema.model_validate_json(response.text)

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Создание нового курса.

        :param request: Pydantic-модель с данными для создания курса.
        :return: Сырой ответ сервера (httpx.Response).
        """
        return self.client.post(
            "/api/v1/courses",
            json=request.model_dump(by_alias=True),
        )

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Создание курса с парсингом ответа.

        :param request: Pydantic-модель с данными для создания курса.
        :return: Распарсенный ответ в виде CreateCourseResponseSchema.
        """
        response = self.create_course_api(request)
        response.raise_for_status()
        return CreateCourseResponseSchema.model_validate_json(response.text)

    def update_course_api(
            self, course_id: str, request: UpdateCourseRequestSchema
    ) -> Response:
        """
        Частичное обновление курса (PATCH).

        :param course_id: UUID курса для обновления.
        :param request: Pydantic-модель с полями для обновления.
        :return: Сырой ответ сервера (httpx.Response).
        """
        return self.client.patch(
            f"/api/v1/courses/{course_id}",
            json=request.model_dump(by_alias=True, exclude_unset=True),
        )

    def update_course(
            self, course_id: str, request: UpdateCourseRequestSchema
    ) -> UpdateCourseResponseSchema:
        """
        Частичное обновление курса с парсингом ответа.

        :param course_id: UUID курса для обновления.
        :param request: Pydantic-модель с полями для обновления.
        :return: Распарсенный ответ в виде UpdateCourseResponseSchema.
        """
        response = self.update_course_api(course_id, request)
        response.raise_for_status()
        return UpdateCourseResponseSchema.model_validate_json(response.text)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Удаление курса по его идентификатору.

        :param course_id: UUID курса для удаления.
        :return: Сырой ответ сервера (httpx.Response).
        """
        return self.client.delete(f"/api/v1/courses/{course_id}")


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Фабричная функция: создаёт авторизованный CoursesClient.

    :param user: Данные пользователя для авторизации (email + password).
    :return: Готовый к использованию CoursesClient с настроенным токеном.
    """
    return CoursesClient(client=get_private_http_client(user))