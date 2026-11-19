import allure
from typing import Any, Sized

from tools.logger import get_logger

logger = get_logger("BASE_ASSERTIONS")

@allure.step("Check that response status code equals to {expected}")
def assert_status_code(actual: int, expected: int) -> None:
    logger.info(f"Check that response status code equals to {expected}")
    assert actual == expected, (
        'Incorrect response status code. '
        f'Expected: {expected}. ' 
        f'Actual: {actual}. '
    )
@allure.step("Check that {name} equals to {expected}")
def assert_equal(actual: Any, expected: Any, name: str):
    logger.info(f'Check that "{name}" equals to {expected}')
    assert actual == expected, (
        f'Incorrect value: "{name}". '
        f'Expected: {expected}. ' 
        f'Actual: {actual}. '
    )
@allure.step("Check that {name} is true")
def assert_is_true(actual: Any, name: str):
    logger.info(f'Check that "{name}" is true')
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )

def assert_length(actual: Sized, expected: Sized, name: str):
    with allure.step(f"Check that length of {name} equals to {len(expected)}"):
        logger.info(f'Check that length of "{name}" equals to {len(expected)}')
        assert len(actual) == len(expected), (
        f'Incorrect length: "{name}".'
        f'Expected: {len(expected)}.' 
        f'Actual: {len(actual)}.'
    )