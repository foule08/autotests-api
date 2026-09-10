from client.api_client import ApiClient
from httpx import Response

class CreateFileRequestDict(TypedDict):
    title: str
    maxScore: str
    minScore: str
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateFileRequestDict(TypedDict):
    title: str
    maxScore: str
    inScore: str
    description: str
    estimatedTime: str


class CoursesClient(ApiClient):
    def get_courses_api(self, query: GetCoursesQueryDict):
        return self.get("api/v1/courses", params=query)

    def get_courses_api(self, course_id: str):
        return self.get(f"api/v1/courses/{course_id}")

    def create_courses_api(self, request):
        return self.post("api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict):
        return self.patch(f"api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str):
        return self.delete(f"api/v1/courses/{course_id}")
