import dataclasses
from typing import Any
from datetime import datetime


@dataclasses.dataclass
class Article:
    id: str | None
    label: str | None
    price: str | None
    image_uri: str | None
    description: str | None
    create_at: datetime.datetime | None
    update_at: datetime.datetime | None

    def to_json(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "label": self.label,
            "price": self.price,
            "image_uri": self.image_uri,
            "description": self.description,
            "create_at": self.create_at,
            "update_at": self.update_at
        }