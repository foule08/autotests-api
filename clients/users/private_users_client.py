from httpx import URL
from typing import TypedDict
import allure
from clients.api_client import ApiClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.user_schema import GetUserResponseSchema, UpdateUserRequestSchema
from tools.routes import APIRoutes

class PrivateUsersClient(ApiClient):
    @allure.step("Get current user")
    def get_user_me_api(self):
        return self.get(APIRoutes.USER_ME)

    @allure.step("Get user by id {user_id}")
    def get_get_user_me_api(self, user_id: str):
        return self.get(APIRoutes.USER_BY_ID.value.format(user_id=user_id))

    @allure.step("Update user by id {user_id}")
    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema):
        return self.patch(APIRoutes.USER_BY_ID.value.format(user_id=user_id), json=request.model_dump(by_alias=True))

    @allure.step("Delete user by id {user_id}")
    def delete_user_api(self, user_id: str):
        return self.delete(APIRoutes.USER_BY_ID.value.format(user_id=user_id))

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_get_user_me_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    return PrivateUsersClient(client = get_private_http_client(user))


