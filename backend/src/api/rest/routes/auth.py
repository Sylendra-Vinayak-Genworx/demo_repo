from fastapi import APIRouter, HTTPException, status

from src.core.services.auth_service import AuthService

from ....data.repositories.user_repository import UserRepository
from ....schemas.user import UserCreate, UserResponse

router = APIRouter()

_auth_service = AuthService(UserRepository())


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(payload: UserCreate) -> UserResponse:
    try:
        user = _auth_service.register_user(payload)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))

    return UserResponse(email=user.email)
