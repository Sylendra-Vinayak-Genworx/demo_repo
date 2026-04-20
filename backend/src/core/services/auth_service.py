from passlib.context import CryptContext

from ...data.repositories.user_repository import UserRepository, UserRecord
from ...schemas.user import UserCreate

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


class AuthService:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def register_user(self, user_create: UserCreate) -> UserRecord:
        existing_user = self._repository.get_by_email(user_create.email)
        if existing_user is not None:
            raise ValueError("User already exists")

        password_hash = hash_password(user_create.password)
        return self._repository.create(user_create.email, password_hash)
