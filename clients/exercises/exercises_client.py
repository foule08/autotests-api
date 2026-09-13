from clients.api_client import ApiClient

from typing import TypedDict

from httpx import Request

class GetExercisesDict(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateCourseRequestDict(TypedDict):
    title: str
    maxScore: int
    inScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExerciseClient(ApiClient):
    def get_exercises_api(self, request: GetExercisesDict):
        return self.get("api/v1/exercises", json=request)

    def get_courses_api(self, exercise_id: str):
        return self.get(f"api/v1/exercises/{exercise_id}")

    def create_exercises_api(self, request):
        return self.post("api/v1/exercises", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict):
        return self.patch(f"api/v1/exercises/{exercise_id}", json=request)

    def delete_course_api(self, course_id: str):
        return self.delete(f"api/v1/exercises/{exercise_id}")

