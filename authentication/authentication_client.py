from httpx import Response

from clients.api_client import ApiClient
from typing import TypedDict

class LoginRequestDict(TypedDict):
    email: str
    password: str

class RefreshedRequestDict(TypedDict):
    refreshToken: str

class AuthenticationClient(ApiClient):
    def login_api(self, request: LoginRequestDict) -> Response:
        return self.post("/api/v1/authentication/login", json=request)
    def refresh_api(self, request: RefreshedRequestDict) -> Response:
        return self.post("/api/v1/authentication/refresh", json=request)


client = AuthenticationClient()
client.login_api({'email': '', 'password': ''})