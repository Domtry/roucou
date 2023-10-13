from fastapi import APIRouter

from src.api.endpoints import login

api_route = APIRouter(prefix = "/api/v1")
api_route.include_router(login.route, prefix = "/login", tags = ["Login"])