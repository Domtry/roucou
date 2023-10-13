from fastapi import FastAPI

from src.api.routes import api_route


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_route)
    return app
