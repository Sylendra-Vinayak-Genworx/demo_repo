from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class UserRecord:
    email: str
    password_hash: str


class UserRepository:
    def __init__(self) -> None:
        self._users: Dict[str, UserRecord] = {}

    def create(self, email: str, password_hash: str) -> UserRecord:
        if email in self._users:
            raise ValueError("User already exists")

        user = UserRecord(email=email, password_hash=password_hash)
        self._users[email] = user
        return user

    def get_by_email(self, email: str) -> Optional[UserRecord]:
        return self._users.get(email)
