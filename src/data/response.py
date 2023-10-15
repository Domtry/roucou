import dataclasses
from typing import Any


@dataclasses.dataclass
class Response:
    data: Any
    success: bool
    message: str
