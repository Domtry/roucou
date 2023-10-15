from typing import Any

from fastapi import APIRouter, HTTPException
from starlette import status

from src.core.presenters import schemas
from src.api.composers import LoginComposer
from src.data import https

route = APIRouter()
composer = LoginComposer()


@route.post(
    "/login", response_model = schemas.LoginOut | Any, status_code = status.HTTP_200_OK)
def login_access_token(login: schemas.LoginIn) -> https.HTTPResponse:
    response = composer.auth(login)
    return response


@route.post("/refresh-token", status_code = status.HTTP_200_OK)
def refresh_token() -> https.HTTPResponse:
    return https.HTTPResponse(
        code_status = status.HTTP_404_NOT_FOUND,
        message = "Method not found",
        data = None,
        success = False
    )


@route.post("/logout", status_code = status.HTTP_200_OK)
def refresh_token() -> https.HTTPResponse:
    return https.HTTPResponse(
        code_status = status.HTTP_404_NOT_FOUND,
        message = "Method not found",
        data = None,
        success = False
    )
