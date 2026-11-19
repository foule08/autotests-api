from httpx import Response
import allure

from clients.api_client import ApiClient
from clients.exercises.exercises_schema import (
    GetExercisesQuerySchema,
    GetExercisesResponseSchema,
    GetExerciseResponseSchema,
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
)
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from tools.routes import APIRoutes


class ExercisesClient(ApiClient):
    """
    Клиент для работы с эндпоинтом /api/v1/exercises.
    """

    @allure.step("Get exercises")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Получение списка упражнений по courseId.

        :param query: Pydantic-модель с параметром courseId.
        :return: Сырой ответ сервера (httpx.Response).
        """
        # ✅ Обращаемся к полю через точку, используем by_alias для camelCase
        return self.get(
            APIRoutes.EXERCISES,
            params=query.model_dump(by_alias=True, exclude_none=True),
        )

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Получение списка упражнений с парсингом ответа в Pydantic-модель.

        :param query: Pydantic-модель с параметром courseId.
        :return: Распарсенный ответ в виде GetExercisesResponseSchema.
        """
        response = self.get_exercises_api(query)
        response.raise_for_status()
        return GetExercisesResponseSchema.model_validate_json(response.text)

    @allure.step("Get exercise by id {exercise_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение одного упражнения по ID.

        :param exercise_id: UUID упражнения.
        :return: Сырой ответ сервера (httpx.Response).
        """
        return self.get(APIRoutes.EXERCISE_BY_ID.value.format(exercise_id=exercise_id))

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Получение одного упражнения с парсингом ответа.

        :param exercise_id: UUID упражнения.
        :return: Распарсенный ответ в виде GetExerciseResponseSchema.
        """
        response = self.get_exercise_api(exercise_id)
        response.raise_for_status()
        return GetExerciseResponseSchema.model_validate_json(response.text)

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Создание нового упражнения.

        :param request: Pydantic-модель с данными для создания.
        :return: Сырой ответ сервера (httpx.Response).
        """
        return self.post(
            APIRoutes.EXERCISES,
            json=request.model_dump(by_alias=True),
        )

    def create_exercise(
        self, request: CreateExerciseRequestSchema
    ) -> CreateExerciseResponseSchema:
        """
        Создание упражнения с парсингом ответа.

        :param request: Pydantic-модель с данными для создания.
        :return: Распарсенный ответ в виде CreateExerciseResponseSchema.
        """
        response = self.create_exercise_api(request)
        response.raise_for_status()
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    @allure.step("Update exercise by id {exercise_id}")
    def update_exercise_api(
        self, exercise_id: str, request: UpdateExerciseRequestSchema
    ) -> Response:
        """
        Частичное обновление упражнения (PATCH).

        :param exercise_id: UUID упражнения.
        :param request: Pydantic-модель с полями для обновления.
        :return: Сырой ответ сервера (httpx.Response).
        """
        # ✅ exclude_unset=True — отправляем только явно заданные поля
        return self.patch(
            APIRoutes.EXERCISE_BY_ID.value.format(exercise_id=exercise_id),
            json=request.model_dump(by_alias=True, exclude_unset=True),
        )

    def update_exercise(
        self, exercise_id: str, request: UpdateExerciseRequestSchema
    ) -> UpdateExerciseResponseSchema:
        """
        Частичное обновление упражнения с парсингом ответа.

        :param exercise_id: UUID упражнения.
        :param request: Pydantic-модель с полями для обновления.
        :return: Распарсенный ответ в виде UpdateExerciseResponseSchema.
        """
        response = self.update_exercise_api(exercise_id, request)
        response.raise_for_status()
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

    @allure.step("Delete exercise by id {exercise_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаление упражнения по ID.

        :param exercise_id: UUID упражнения.
        :return: Сырой ответ сервера (httpx.Response).
        """
        # ✅ Исправлена опечатка: exercises (с 's')
        return self.delete(APIRoutes.EXERCISE_BY_ID.value.format(exercise_id=exercise_id))


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Фабричная функция: создаёт авторизованный ExercisesClient.

    :param user: Данные пользователя для авторизации.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))