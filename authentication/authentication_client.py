from httpx import Response

from clients.api_client import ApiClient
from typing import TypedDict

from clients.public_http_builder import get_public_http_client


class LoginRequestDict(TypedDict):
    email: str
    password: str

class RefreshedRequestDict(TypedDict):
    refreshToken: str

class Token(TypedDict):
    tokenType: str
    accessToken: str
    refreshToken: str

class LoginResponseDict(TypedDict):
    token: Token

class AuthenticationClient(ApiClient):
    def login_api(self, request: LoginRequestDict) -> Response:
        return self.post("/api/v1/authentication/login", json=request)
    def refresh_api(self, request: RefreshedRequestDict) -> Response:
        return self.post("/api/v1/authentication/refresh", json=request)
    def login_api(self, request: LoginRequestDict) -> Response:
        return self.client.post("/api/v1/authentication/login", json=request)
        return response.json()


def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())