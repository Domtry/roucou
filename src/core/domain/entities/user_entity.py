import datetime
import dataclasses
from typing import Any

@dataclasses.dataclass
class Users:
    id: str | None
    name: str | None
    phone: str | None
    email: str | None
    address: str | None
    create_at: datetime.datetime | None
    update_at: datetime.datetime | None

    def to_json(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "create_at": self.create_at,
            "update_at": self.update_at
        }
