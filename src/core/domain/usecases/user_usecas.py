from src import data
from src.core.domain import entities


class UserUsecase:
    def create(self, user: entities.Users) -> data.Response :
        raise Exception("Please implement this method")

    def get_one(self, user_id: str) -> data.Response:
        raise Exception("Please implement this method")

    def find_by_email(self, email:str) -> data.Response:
        raise Exception("Please implement this method")

    def find_by_phone(self, email:str) -> data.Response:
        raise Exception("Please implement this method")

    def find_by_id(self, user_id: str) -> data.Response:
        raise Exception("Please implement this method")