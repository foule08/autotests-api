from enum import Enum


class APIRoutes(str, Enum):
    USERS = "/api/v1/users"
    USER_ME = "/api/v1/users/me"
    USER_BY_ID = "/api/v1/users/{user_id}"
    AUTHENTICATION_LOGIN = "/api/v1/authentication/login"
    AUTHENTICATION_REFRESH = "/api/v1/authentication/refresh"
    FILES = "/api/v1/files"
    FILE_BY_ID = "/api/v1/files/{file_id}"
    COURSES = "/api/v1/courses"
    COURSE_BY_ID = "/api/v1/courses/{course_id}"
    EXERCISES = "/api/v1/exercises"
    EXERCISE_BY_ID = "/api/v1/exercises/{exercise_id}"

    def __str__(self):
        return self.value