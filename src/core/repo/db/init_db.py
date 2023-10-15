from fastapi import FastAPI

from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def init_db(engine: Engine, app: FastAPI | None = None):
    try:
        from src.core.repo.models import (
            UsersModel
        )
        Base.metadata.create_all(bind = engine, checkfirst = True)

    except Exception as error:
        print(error)
        Base.metadata.drop_all(bind = engine)
