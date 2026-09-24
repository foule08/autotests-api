from pydantic import BaseModel, HttpUrl

class CreateFileRequestSchema(BaseModel):
    filename: str
    directory: str
    upload_file: str

class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str

class CreateFileResponseSchema(BaseModel):
    file: FileSchema