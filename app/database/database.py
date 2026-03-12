from typing import List

from app.models.session import Session
from app.models.user import User


class Database:
    def __init__(self) -> None:
        self.users: List[User] = []
        self.sessions: List[Session] = []
