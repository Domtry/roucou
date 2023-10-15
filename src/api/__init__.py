from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import api_route
from src.core.repo.db import DBHandler, init_db

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
]


def create_app() -> FastAPI:
    app = FastAPI(
        title = "Roucou API",
        description = "Roucou API",
        summary = "Deadpool's favorite app. Nuff said.",
        version = "0.0.1",
        terms_of_service = "https://example.com/terms/",
        contact = {
            "name": "Dycode SA",
            "url": "https://x-force.example.com/contact/",
            "email": "doffoufaye@gmail.com",
        },
        license_info = {
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
    )

    app.add_middleware(CORSMiddleware, allow_origins = origins,
                       allow_credentials = True,
                       allow_methods = ["*"],
                       allow_headers = ["*"], )

    engine = DBHandler().get_engine()
    init_db(engine)

    app.include_router(api_route)
    return app
