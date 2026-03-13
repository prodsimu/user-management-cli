from typing import Optional

from app.models.session import Session
from app.models.user import User
from app.seed.seed import Seed
from app.services.session_service import SessionService
from app.services.user_service import UserService


class AppController:

    def __init__(
        self,
        user_service: UserService,
        session_service: SessionService,
    ) -> None:

        self.user_service: UserService = user_service
        self.session_service: SessionService = session_service

        self.current_session: Optional[Session] = None
        self.current_user: Optional[User] = None

    # INITIALIZATION

    def bootstrap(self) -> None:
        seed = Seed(self.user_service)
        admin = seed.run_seed()

        if admin:
            self.current_user = admin
            self.current_session = self.session_service.create_session(admin.id)

    # CREATE

    def create_user(self, name: str, username: str, password: str) -> User:
        return self.user_service.create_user(name, username, password)

    # READ

    def get_current_user(self) -> Optional[User]:
        if self.current_session:
            return self.user_service.get_user_by_id(self.current_session.user_id)

        return None

    def list_all_users(self) -> list[User]:
        return self.user_service.list_all_users()

    # UPDATE

    def update_password(self, user_id: int, new_password: str) -> None:
        self.user_service.update_password_by_id(user_id, new_password)

    def update_name(self, user_id: int, new_name: str) -> None:
        self.user_service.update_name_by_id(user_id, new_name)

    def update_username(self, user_id: int, new_username: str) -> None:
        self.user_service.update_username_by_id(user_id, new_username)

    # DELETE

    def delete_user(self, user_id: int) -> None:
        self.user_service.delete_user_by_id(user_id)

    # AUTHENTICATION

    def login(self, username: str, password: str) -> Optional[Session]:
        session = self.user_service.login(username, password)

        self.current_session = session
        self.current_user = self.user_service.get_user_by_id(session.user_id)

        return session

    def logout(self) -> None:
        if self.current_session:
            self.session_service.logout(self.current_session.id)

        self.current_session = None
        self.current_user = None

    # UTILS

    def has_active_session(self) -> bool:
        return self.current_session is not None

    def is_admin(self) -> bool:
        return self.current_user is not None and self.current_user.role == "admin"
