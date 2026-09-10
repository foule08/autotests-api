from httpx import Response
from typing import TypedDict
from clients.api_client import ApiClient

class UpdateUserRequestDict(TypedDict):
    email: str
    lastName: str
    firtName: str
    middleName: str

class PrivateUsersClient(ApiClient):
    def get_get_user_me_api(self):
        return self.get(/api/v1/users/me)

    def get_get_user_me_api(self, user_id: str):
        return self.get(/api/v1/users//me//{user_id})

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict):
        return self.put(/api/v1/users/me/{user_id}, json=request)

    def delete_user_api(self, user_id: str):
        return self.delete(/api/v1/users//me/{user_id})