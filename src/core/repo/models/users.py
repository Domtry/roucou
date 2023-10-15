from .abstract_model import AbstractModel
from sqlalchemy import (
    Column,
    String,
)

from src.core.repo.db import Base


class UsersModel(AbstractModel, Base):
    __tablename__ = "users_model_db"
    __table_args__ = {'extend_existing': True}

    name = Column(String, nullable = False)
    phone = Column(String, nullable = False, unique = True)
    email = Column(String, nullable = False, unique = True)
    address = Column(String, default = 0, nullable = False)
