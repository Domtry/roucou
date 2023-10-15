import datetime
from uuid import uuid4
from typing import Any

from src.core.domain import entities
from src.core.presenters.factories import AbstractFactories
from src.core.repo import models


class UserFactory(AbstractFactories):
    @classmethod
    def to_object(cls, json_object: dict[str, Any]) -> entities.Users:
        return entities.Users(
            id = str(uuid4()),
            name = json_object["name"],
            address = json_object["address"],
            phone = json_object["phone"],
            email = json_object["email"],
            create_at = datetime.datetime.now(),
            update_at = datetime.datetime.now(),
        )


    @classmethod
    def to_model(cls, object: entities.Users) -> models.UsersModel:
        return models.UsersModel(
            id = object.id,
            name = object.name,
            phone = object.phone,
            address = object.address,
            email = object.email,
            create_at = object.create_at,
            update_at = object.update_at
        )
    @classmethod
    def to_json(cls, object: entities.Users) -> dict[str, Any]:
        return {
            "id": object.id,
            "name": object.name,
            "address": object.address,
            "phone": object.phone,
            "email": object.email,
            "create_at": object.create_at,
            "update_at": object.update_at
        }


    @classmethod
    def convert_to_object(cls, model: models.UsersModel) -> entities.Users:
        return entities.Users(
            id = model.id,
            email = model.email,
            phone = model.phone,
            name = model.name,
            address = model.address,
            create_at = model.create_at,
            update_at = model.update_at
        )
