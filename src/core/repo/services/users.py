from typing import Any

from sqlalchemy import select

from src import data
from src.core.domain import entities
from src.core.domain.usecases import UserUsecase
from src.core.presenters import factories
from src.core.repo.models import UsersModel
from src.core.repo.db import DBHandler


class UserService(UserUsecase):
    def create(self, user: entities.Users) -> data.Response:
        with DBHandler() as db_cursor:
            try:
                factory = factories.UserFactory
                user_model = factory.to_model(user)

                db_cursor.session.add(user_model)
                db_cursor.session.commit()

                user_entity = factory.convert_to_object(user_model)
                return data.Response(
                    data = user_entity,
                    success = True,
                    message = "Utilisateur créé avec succès"
                )

            except Exception as err:
                db_cursor.session.rollback()
                return data.Response(
                    data = None,
                    success = False,
                    message = err.args[0]
                )

    def find_by_phone(self, phone: str) -> data.Response:
        with DBHandler() as db_cursor:
            try:
                factory = factories.UserFactory
                stmt = select(UsersModel).where(
                    UsersModel.phone == phone
                )

                if not (stmt_resp := db_cursor.session.execute(stmt).first()):
                    return data.Response(
                        data = None,
                        success = False,
                        message = "Nous n'avons trouvé aucune donnée correspondant à ce numéro"
                    )

                user_entity = factory.convert_to_object(stmt_resp[0])
                return data.Response(
                    data = user_entity,
                    success = True,
                    message = "Utilisateur récupéré avec succès"
                )

            except Exception as err:
                print("Exception :::> ", err)
                return data.Response(
                    data = None,
                    success = False,
                    message = err.args[0]
                )

    def find_by_email(self, email: str) -> data.Response:
        db_cursor: DBHandler
        with DBHandler() as db_cursor:
            try:
                factory = factories.UserFactory
                stmt = select(UsersModel).where(
                    UsersModel.email == email
                )

                if not (stmt_resp := db_cursor.session.execute(stmt).first()):
                    return data.Response(
                        data = None,
                        success = False,
                        message = "Nous n'avons trouvé aucune donnée correspondant à ce numéro"
                    )

                user_entity = factory.convert_to_object(stmt_resp[0])

            except Exception as error:
                print("error detected :::> ", error.args[0])
                return data.Response(
                    data = None,
                    success = False,
                    message = "Nous avons rencontré un problème durant la sauvegarde."
                )
            else:
                return data.Response(
                    data = user_entity,
                    success = True,
                    message = "Utilisateur récupéré avec succès"
                )

    def find_by_id(self, user_id: str) -> data.Response:
        db_cursor: DBHandler
        with DBHandler() as db_cursor:
            try:
                factory = factories.UserFactory
                stmt = select(UsersModel).where(
                    UsersModel.id == user_id
                )

                if not (stmt_resp := db_cursor.session.execute(stmt).first()):
                    return data.Response(
                        data = None,
                        success = False,
                        message = "Nous n'avons trouvé aucune donnée correspondant à cette reférence"
                    )

                user_entity = factory.convert_to_object(stmt_resp[0])

            except Exception as error:
                return data.Response(
                    data = None,
                    success = False,
                    message = "Nous avons rencontré un problème durant la récupération de l'utilisateur."
                )
            else:
                return data.Response(
                    data = user_entity,
                    success = True,
                    message = "Utilisateur récupéré avec succès"
                )