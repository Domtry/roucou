import dataclasses
from typing import Any, TypeVar

from pydantic import BaseModel


@dataclasses.dataclass
class HTTPRequest:
    body: BaseModel | None
    query: dict[str, Any]
    headers: dict[str, Any]


@dataclasses.dataclass
class HTTPResponse:
    data: dict[str, Any] | None
    message: str
    success: bool
    code_status: int
