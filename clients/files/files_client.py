from clients.api_client import ApiClient

from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema

class FilesClient(ApiClient):
    def get_file_api(self, file_id: str):
        return self.get(f"api/v1/files/{file_id}")

    def create_file_api(self, request):
        return self.post(
            "api/v1/files",
            data = request.model_dump(by_alias=True, exclude={'upload_file'}),
            files = {"upload_file": open(request.upload_file, 'rb')}
        )
    def create_file(self,request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)

    def delete_file_api(self, file_id: str):
        return self.delete(f"api/v1/files/{file_id}")

def get_files_client(user: AuthenticationUserSchema):
    return FilesClient(client = get_private_http_client(user))