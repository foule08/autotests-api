from httpx import URL
from typing import TypedDict
from clients.api_client import ApiClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.user_schema import GetUserResponseSchema, UpdateUserRequestSchema

class PrivateUsersClient(ApiClient):
    def get_user_me_api(self):
        return self.get('/api/v1/users/me')

    def get_get_user_me_api(self, user_id: str):
        response = self.get(f"/api/v1/users/{user_id}")
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema):
        return self.patch(f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True))

    def delete_user_api(self, user_id: str):
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_get_user_me_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    return PrivateUsersClient(client = get_private_http_client(user))


