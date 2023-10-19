from typing import Any

from fastapi import APIRouter
from starlette import status

from src.api.composers import ArticleComposer
from src.core.presenters import schemas
from src.data import https

route = APIRouter()
composer = ArticleComposer()


@route.post("/register", response_model = https.HTTPResponse | Any)
async def register_article(article: schemas.ArticleIn) -> https.HTTPResponse:
    response = composer.register_user(article)
    return https.HTTPResponse(
        data = response.data,
        message = response.message,
        success = response.success,
        code_status = status.HTTP_404_NOT_FOUND
    )


@route.put("/update/{article_id}", response_model = https.HTTPResponse | Any)
async def register_article(article_id: str, article: schemas.ArticleIn) -> https.HTTPResponse:
    return https.HTTPResponse(
        data = None,
        message = "Method not found",
        success = False,
        code_status = status.HTTP_404_NOT_FOUND
    )


@route.get("/pagination/{skip}/{limit}", response_model = https.HTTPResponse | Any)
async def register_article(skip: int, limit: int) -> https.HTTPResponse:
    return https.HTTPResponse(
        data = None,
        message = "Method not found",
        success = False,
        code_status = status.HTTP_404_NOT_FOUND
    )


@route.get("/{article_id}", response_model = https.HTTPResponse | Any)
async def get_article(article_id: str) -> https.HTTPResponse:
    return https.HTTPResponse(
        data = None,
        message = "Method not found",
        success = False,
        code_status = status.HTTP_404_NOT_FOUND
    )
