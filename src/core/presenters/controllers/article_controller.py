from src import data
from src.core.domain import entities
from src.core.repo.services import ArticleService

repo = ArticleService()


class ArticleControllers:
    @classmethod
    def register(cls, repo: ArticleService, article: entities.Article) -> data.Response:
        result = repo.create(article)
        if not result.success:
            return data.Response(
                data = None,
                success = False,
                message = data.message
            )

        return data.Response(
            data = result.data,
            success = result.success,
            message = result.message
        )
