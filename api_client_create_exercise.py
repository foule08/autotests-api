from clients.courses.courses_client import CreateCourseRequestSchema, get_courses_client
from clients.exercises.exercises_client import (
    CreateExerciseRequestSchema,
    get_exercises_client,
)
from clients.files.files_client import CreateFileRequestSchema, get_files_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema  # ← один импорт
from tools.fakers import get_random_email


public_users_client = get_public_users_client()

user_to_create = CreateUserRequestSchema(
    email=get_random_email(),
    password="123123",
    firstName="john",
    lastName="doe",
    middleName="doee",
)

create_user_response = public_users_client.create_user(user_to_create)
print("Create user data:", create_user_response)


authentication_user = AuthenticationUserSchema(
    email=user_to_create.email,
    password=user_to_create.password,
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)


# 3. Загружаем файл
file_to_create = CreateFileRequestSchema(
    filename="pibbel.png",
    directory="files",
    upload_file="testdata/files/pibbel.png",
)

create_file_response = files_client.create_file(file_to_create)
print("Create file data:", create_file_response)



course_to_create = CreateCourseRequestSchema(
    title="API",
    maxScore=100,
    minScore=10,
    description="API Automation testing",
    estimatedTime="2 week",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id,
)

create_course_response = courses_client.create_course(course_to_create)
print("Create course data:", create_course_response)


create_exercise_request = CreateExerciseRequestSchema(
    title="API Exercise",
    courseId=create_course_response.course.id,
    maxScore=100,
    minScore=10,
    orderIndex=1,
    description="Api automation exercise",
    estimatedTime="24 h",
)

create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print("Create exercise data:", create_exercise_response)

