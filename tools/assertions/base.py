from typing import Any, Sized

def assert_status_code(actual: int, expected: int) -> None:
    assert actual == expected, (
        'Incorrect response status code. '
        f'Expected: {expected}. ' 
        f'Actual: {actual}. '
    )
def assert_equal(actual: Any, expected: Any, name: str):
    assert actual == expected, (
        f'Incorrect value: "{name}". '
        f'Expected: {expected}. ' 
        f'Actual: {actual}. '
    )
def assert_is_true(actual: Any, name: str):
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )

def assert_length(actual, expected, name: str):
    assert len(actual) == len(expected), (
        f'Incorrect length: "{name}".'
        f'Expected: {len(expected)}.' 
        f'Actual: {len(actual)}.'
    )