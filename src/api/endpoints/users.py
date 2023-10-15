from typing import Any

from fastapi import APIRouter, HTTPException
from starlette import status

from src.core.presenters import schemas
from src.api.composers import UserComposer
from src.data import HTTPResponse

route = APIRouter()


@route.post("/register", response_model = Any, status_code = status.HTTP_201_CREATED)
async def register_user(user: schemas.UserIn) -> HTTPResponse:
    return UserComposer.register_user(user)


@route.put("/update/{user_id}", response_model = Any, status_code = status.HTTP_202_ACCEPTED)
async def update_profil(user_id: str, user: schemas.UserIn) -> HTTPException:
    return HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Method has not implemented"
    )


@route.get('/me', response_model = Any, status_code = status.HTTP_200_OK)
def profil() -> HTTPException:
    return HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Method has not implemented"
    )


@route.get("/{user_id}", response_model = Any, status_code = status.HTTP_200_OK)
async def user_detail(user_id: str) -> HTTPResponse:
    return UserComposer.get_user_by_id(user_id)
