import allure
from typing import Any, Sized

@allure.step("Check that response status code equals to {expected}")
def assert_status_code(actual: int, expected: int) -> None:
    assert actual == expected, (
        'Incorrect response status code. '
        f'Expected: {expected}. ' 
        f'Actual: {actual}. '
    )
@allure.step("Check that {name} equals to {expected}")
def assert_equal(actual: Any, expected: Any, name: str):
    assert actual == expected, (
        f'Incorrect value: "{name}". '
        f'Expected: {expected}. ' 
        f'Actual: {actual}. '
    )
@allure.step("Check that {name} is true")
def assert_is_true(actual: Any, name: str):
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )

def assert_length(actual: Sized, expected: Sized, name: str):
    with allure.step(f"Check that length of {name} equals to {len(expected)}"):
     assert len(actual) == len(expected), (
        f'Incorrect length: "{name}".'
        f'Expected: {len(expected)}.' 
        f'Actual: {len(actual)}.'
    )