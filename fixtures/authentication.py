import pytest

from authentication.authentication_client import get_authentication_client


@pytest.fixture
def authentication_client():
    return get_authentication_client()