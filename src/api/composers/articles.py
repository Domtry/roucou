from starlette import status

from src.core.presenters import schemas
from src.core.presenters.controllers import ArticleControllers
from src.core.presenters.factories import ArticleFactory
from src.core.repo.services import ArticleService
from src.data import https

repo = ArticleService()
class ArticleComposer:

    @classmethod
    def register_user(cls, user: schemas.ArticleIn) -> https.HTTPResponse:
        article_entity =  ArticleFactory.to_object(user.dict())
        response = ArticleControllers.register(repo, article_entity)

        if not response.success:
            return https.HTTPResponse(
                data = response.data,
                message = response.message,
                success = response.success,
                code_status = status.HTTP_400_BAD_REQUEST
            )

        return https.HTTPResponse(
            data = response.data,
            message = response.message,
            success = response.success,
            code_status = status.HTTP_201_CREATED
        )
