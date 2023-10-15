from typing import Any


class AbstractFactories:
    @classmethod
    def to_json(cls, object: Any) -> dict[str, Any]:
        ...

    @classmethod
    def to_object(cls, json_object: dict[str, Any]) -> Any:
        ...

    @classmethod
    def to_model(cls, object: Any) -> Any:
        ...

    @classmethod
    def convert_to_object(cls, model: Any) -> Any:
        ...
