import allure

from clients.users.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, \
    InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length


@allure.step("Check validation error")
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.location, expected.location, "location")

@allure.step("Check validation error response")
def assert_validation_error_response(actual: ValidationErrorResponseSchema, expected: ValidationErrorResponseSchema):
    assert_length(actual.details, expected.details, "details")

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)

@allure.step("Check create file with empty filename response")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "filename"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)

@allure.step("Check create file with empty directory response")
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "directory"]
            )
        ]
     )
    assert_validation_error_response(actual, expected)

@allure.step("Check internal error response")
def assert_internal_error_response(actual: InternalErrorResponseSchema, expected: InternalErrorResponseSchema):
    assert_equal(actual.details, expected.details, "details")