from httpx import Client
from authentication.authentication_client import get_authentication_client, LoginRequestSchema
from pydantic import BaseModel

class AuthenticationUserSchema(BaseModel):
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserSchema):
    authentication_client = get_authentication_client()

    login_request = LoginRequestSchema(email = user.email, password = user.password)
    login_response = authentication_client.login(login_request)


    return Client(
        timeout=100,
        base_url="http://127.0.0.1:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )