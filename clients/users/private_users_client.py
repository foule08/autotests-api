from httpx import URL
from typing import TypedDict
from clients.api_client import ApiClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class UpdateUserRequestDict(TypedDict):
    email: str
    lastName: str
    firstName: str
    middleName: str

class User(TypedDict):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class GetUserResponseDict(TypedDict):
    user: User

class PrivateUsersClient(ApiClient):
    def get_user_me_api(self):
        return self.get('/api/v1/users/me')

    def get_get_user_me_api(self, user_id: str):
        response = self.get(f"/api/v1/users/{user_id}")
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict):
        return self.patch(URL(f"/api/v1/users/{user_id}"), json=request)

    def delete_user_api(self, user_id: str):
        return self.delete(URL(f"/api/v1/users/{user_id}"))

    def get_user(self, user_id: str) -> GetUserResponseDict:
        response = self.get_get_user_me_api(user_id)
        return response.json()

def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    return PrivateUsersClient(client = get_private_http_client(user))


