from pydantic import BaseModel, Field


class TokenSchema(BaseModel):
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')

class LoginRequestSchema(BaseModel):
    email: str = Field(alias='email')
    password: str = Field(alias='password')

class RefreshedRequestSchema(BaseModel):
    refresh_token: str = Field(alias='refreshToken')

class LoginResponseSchema(BaseModel):
    token: TokenSchema