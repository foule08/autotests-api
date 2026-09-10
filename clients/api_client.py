from httpx import Client, URL, QueryParams, Response
from typing import Any

from httpx.types import RequestData, RequestFiles

class ApiClient:
    def __init__(self, client: Client):
        self.client = client

        def get(self, url: URL, params: QueryParams):
            return self.client.get(url, params=params)
            """
            Выполняет GET-запрос.

            :param url: URL-адрес эндпоинта.
            :param params: GET-параметры запроса (например, ?key=value).
            :return: Объект Response с данными ответа.
            """

        def post(self, url: URL, json: Any, data: RequestData, files: RequestFiles):
            return self.client.post(url, json=json, data=data, files=files)
            """
            Выполняет POST-запрос.

            :param url: URL-адрес эндпоинта.
            :param json: Данные в формате JSON.
            :param data: Форматированные данные формы (например, application/x-www-form-urlencoded).
            :param files: Файлы для загрузки на сервер.
            :return: Объект Response с данными ответа.
            """

        def patch(self, url: URL, json: Any):
            return self.client.patch(url, json=json)

            """
            Выполняет PATCH-запрос (частичное обновление данных).

            param url: URL-адрес эндпоинта.
            :param json: Данные для обновления в формате JSON.
            :return: Объект Response с данными ответа.
            """
        def delete(self, url: URL):
            return self.client.delete(url)

            """
            Выполняет DELETE-запрос (удаление данных).

            :param url: URL-адрес эндпоинта.
            :return: Объект Response с данными ответа.
            """