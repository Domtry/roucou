from starlette import status

from src.core.presenters import schemas
from src.core.presenters.factories import UserFactory
from src.core.presenters.controllers import UserControllers
from src.core.repo.services import UserService
from src.data import https

repo = UserService()


class UserComposer:
    @classmethod
    def register_user(cls, user: schemas.UserIn) -> https.HTTPResponse:
        user_entity = UserFactory.to_object(user.dict())
        response = UserControllers.register(repo, user_entity)

        if not response.success:
            return https.HTTPResponse(
                data = response.data,
                message = response.message,
                success = response.success,
                code_status = status.HTTP_400_BAD_REQUEST
            )

        return https.HTTPResponse(
            data = response.data,
            message = response.message,
            success = response.success,
            code_status = status.HTTP_201_CREATED
        )

    @classmethod
    def get_user_by_id(cls, user_id: str) -> https.HTTPResponse:
        response = UserControllers.get_by_id(repo, user_id)
        if not response.success:
            return https.HTTPResponse(
                data = response.data,
                message = response.message,
                success = response.success,
                code_status = status.HTTP_400_BAD_REQUEST
            )

        return https.HTTPResponse(
            data = response.data,
            message = response.message,
            success = response.success,
            code_status = status.HTTP_200_OK
        )
