from src import data
from src.core.domain import entities
from src.core.domain.usecases import ArticleUsecase
from src.core.presenters import factories
from src.core.repo.db import DBHandler


class ArticleService(ArticleUsecase):
    def create(self, article: entities.Article) -> data.Response:
        with DBHandler() as db_cursor:
            try:
                factory = factories.Article
                article_model = factory.to_model(article)

                db_cursor.session.add(article_model)
                db_cursor.session.commit()

                article_entity = factory.convert_to_object(article_model)
                return data.Response(
                    data = article_entity,
                    success = True,
                    message = "Article créé avec succès"
                )

            except Exception as err:
                db_cursor.session.rollback()
                return data.Response(
                    data = None,
                    success = False,
                    message = err.args[0]
                )