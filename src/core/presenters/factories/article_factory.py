from datetime import datetime
from typing import Any
from uuid import uuid4

from src.core.repo import models
from src.core.domain import entities
from src.core.presenters.factories import AbstractFactories


class ArticleFactory(AbstractFactories):
    @classmethod
    def to_object(cls, json_object: dict[str, Any]) -> entities.Article:
        return entities.Article(
            id = str(uuid4()),
            label = json_object["label"],
            image_uri = json_object["image_uri"],
            description = json_object["description"],
            price = json_object["price"],
            create_at = datetime.now(),
            update_at = datetime.now(),
        )

    @classmethod
    def to_model(cls, object: entities.Article) -> models.ArticleModel:
        return models.ArticleModel(
            id = object.id,
            label = object.label,
            price = object.price,
            image_uri = object.image_uri,
            description = object.description,
            create_at = object.create_at,
            update_at = object.update_at
        )

    @classmethod
    def to_json(cls, object: entities.Article) -> dict[str, Any]:
        return {
            "id": object.id,
            "label": object.label,
            "price": object.price,
            "image_uri": object.image_uri,
            "description": object.description,
            "create_at": object.create_at,
            "update_at": object.update_at
        }

    @classmethod
    def convert_to_object(cls, model: models.ArticleModel) -> entities.Article:
        return entities.Article(
            id = model.id,
            label = model.email,
            price = model.phone,
            image_uri = model.name,
            description = model.address,
            create_at = model.create_at,
            update_at = model.update_at
        )