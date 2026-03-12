from app.controllers.app_controller import AppController
from app.database.database import Database
from app.repositories.session_repository import SessionRepository
from app.repositories.user_repository import UserRepository
from app.services.session_service import SessionService
from app.services.user_service import UserService
from app.ui.cli import CLI


def build_app() -> CLI:
    database = Database()

    session_repo = SessionRepository(database)
    user_repo = UserRepository(database)

    session_service = SessionService(session_repo)
    user_service = UserService(user_repo, session_service)

    app_controller = AppController(user_service, session_service)

    return CLI(app_controller)


def start():
    cli = build_app()
    cli.start_app()


if __name__ == "__main__":
    start()
