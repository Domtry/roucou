from starlette import status

from src.core.presenters import schemas
from src.data import https


class LoginComposer:
    @classmethod
    def auth(cls, login: schemas.LoginIn) -> https.HTTPResponse:
        data = {
            "role": "admin",
            "username": login.username,
            "token": {
                "access_token": "xxxx",
                "refresh_token": "ssss"
            }
        }

        return https.HTTPResponse(
            data = data,
            message = "authenticate message",
            code_status = status.HTTP_200_OK,
            success = True
        )