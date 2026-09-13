from httpx import Client

def get_public_http_client():
    return Client(timeout=100, base_url="http://127.0.0.1:8000")

