import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str = Field(min_length = 3)
    phone: str = Field(min_length = 3)
    email: str
    address: str = Field(default = "", min_length = 3, validate_default = True)


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    id: str = Field(default_factory=lambda: uuid4().hex)
    create_at: datetime.datetime
    update_at: datetime.datetime
