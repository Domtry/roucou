from typing import Any

from fastapi import APIRouter
from starlette import status

from src.core.presenters.schemas import login

route = APIRouter()


@route.post(
    "/access-token", response_model = Any, status_code = status.HTTP_200_OK)
def login_access_token(login: login.LoginIn) -> login.LoginOut:

    return {
        "role": "admin",
        "username": login.username,
        "token": {
            "access_token": "xxxx",
            "refresh_token": "ssss"
        }
    }
