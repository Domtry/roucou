from starlette import status

from src import data
from src.core.domain import entities
from src.core.repo.services import UserService
from src.data import https


class UserControllers:
    @classmethod
    def register(cls, repo: UserService, user: entities.Users) -> data.Response:
        search = repo.find_by_email(user.email)
        if search.success:
            return data.Response(
                data = None,
                message = "Cette adresse email à déjà été utilisé",
                success = False
            )

        search = repo.find_by_phone(user.phone)
        if search.success:
            return data.Response(
                data = None,
                message = "Ce numéro de téléphone à déjà été utilisé",
                success = False
            )

        response = repo.create(user)
        if not response.success:
            return data.Response(
                data = None,
                message = response.message,
                success = False
            )

        return data.Response(
            data = response.data,
            message = response.message,
            success = True
        )

    @classmethod
    def get_by_id(cls, repo: UserService, user_id: str) -> data.Response:
        response = repo.find_by_id(user_id)
        if not response.success:
            return data.Response(
                data = None,
                message = response.message,
                success = response.success
            )

        return data.Response(
            data = response.data,
            message = response.message,
            success = True
        )