from fastapi import APIRouter

from src.api.endpoints import login
from src.api.endpoints import users
from src.api.endpoints import articles


api_route = APIRouter(prefix = "/api/v1")
api_route.include_router(login.route, prefix = "/auth", tags = ["Authentication"])
api_route.include_router(users.route, prefix = "/users", tags = ["User Provisioning"])
api_route.include_router(articles.route, prefix = "/articles", tags = ["Articles"])
