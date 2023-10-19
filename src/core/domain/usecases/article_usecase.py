from src import data
from src.core.domain import entities


class ArticleUsecase :

    def create(self, article: entities.Article) -> data.Response :
        raise Exception("Please implement this method")

