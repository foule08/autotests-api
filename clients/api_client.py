from httpx import Client, Response
from typing import Any, Optional
from httpx._types import RequestData, RequestFiles


class ApiClient:
    def __init__(self, client: Client):
        self.client = client

    def get(self, url: str, params: Optional[dict] = None) -> Response:
        return self.client.get(url, params=params)

    def post(self, url: str, json: Any = None, data: RequestData = None, files: RequestFiles = None) -> Response:
        # Собираем только переданные параметры
        kwargs = {}
        if json is not None:
            kwargs['json'] = json
        if data is not None:
            kwargs['data'] = data
        if files is not None:
            kwargs['files'] = files

        return self.client.post(url, **kwargs)

    def patch(self, url: str, json: Any = None) -> Response:
        return self.client.patch(url, json=json)

    def delete(self, url: str) -> Response:
        return self.client.delete(url)

