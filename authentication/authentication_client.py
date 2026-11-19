from httpx import Response
import allure

from authentication.authentication_schema import LoginRequestSchema, RefreshedRequestSchema, LoginResponseSchema
from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client
from tools.routes import APIRoutes



class AuthenticationClient(ApiClient):

    @allure.step("Authenticate user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        return self.post(
            APIRoutes.AUTHENTICATION_LOGIN,
            json=request.model_dump(by_alias=True)
         )

    @allure.step("Refresh token")
    def refresh_api(self, request: RefreshedRequestSchema) -> Response:
        return self.post(APIRoutes.AUTHENTICATION_REFRESH,
        json=request.model_dump(by_alias=True)
        )

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)



def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())