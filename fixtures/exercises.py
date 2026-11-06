from pydantic import BaseModel
import pytest

from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture

class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema

@pytest.fixture
def exercise_client(function_user: UserFixture):
    return get_exercises_client(function_user.authentication_user)


class ClientFixture:
    pass


@pytest.fixture
def function_exercise(exercises_client, function_course: CourseFixture):   # ← pytest сначала создаст курс
    request = CreateExerciseRequestSchema(courseId=function_course.response.course.id)   # ← берём id реального курс)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
