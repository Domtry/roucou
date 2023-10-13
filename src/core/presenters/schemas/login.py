from pydantic import BaseModel


class LoginBase(BaseModel):
    username: str
    password: str


class LoginIn(LoginBase):
    username: str
    password: str


class TokenBase(BaseModel):
    access_token: str
    refresh_token: str


class LoginOut(LoginBase):
    username: str
    role: str
    token: TokenBase
