from datetime import datetime

from src.core.repo.db import Base
from src.core.repo.models import AbstractModel


class ArticleModel(AbstractModel, Base):
    __tablename__ = "article_model_db"
    __table_args__ = {'extend_existing': True}

    label: str | None
    price: str | None
    image_uri: str | None
    description: str | None
