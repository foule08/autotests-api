import allure

from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileSchema, \
    GetFileResponseSchema
from clients.users.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, \
    InternalErrorResponseSchema
from config import settings
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response
from tools.logger import get_logger

logger = get_logger("FILES_ASSERTIONS")


@allure.step("Check create file response")
def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    logger.info("Check create file response")
    expected_url = f"{settings.http_client.client_url}static/{request.directory}/{request.filename}".replace("localhost", "127.0.0.1")
    actual_url = str(response.file.url).replace("localhost", "127.0.0.1")
    assert_equal(actual_url, expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")

@allure.step("Check file")
def assert_file(actual: FileSchema, expected: FileSchema):
    logger.info("Check file")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")

@allure.step("Check get file response")
def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    logger.info("Check get file response")
    assert_file(get_file_response.file, create_file_response.file)

@allure.step("Check file not found response")
def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    logger.info("Check file not found response")
    expected = InternalErrorResponseSchema(detail="File not found")
    assert_internal_error_response(actual, expected)



@allure.step("Check get file with incorrect file id response")
def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    logger.info("Check get file with incorrect file id response")
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="uuid_parsing",
                input="incorrect-file-id",
                context={"error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"},
                msg="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                loc=["path", "file_id"],
            )
        ]
    )
    assert_validation_error_response(actual, expected)
