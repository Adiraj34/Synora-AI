from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserLogin
)
from app.services.auth_service import (
    register_user,
    get_users,
    login_user
)
from app.utils.token import create_access_token

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return register_user(db, user)


@router.get(
    "/users",
    response_model=list[UserResponse]
)
def users(
    db: Session = Depends(get_db)
):
    return get_users(db)


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    existing_user = login_user(
        db,
        user.email,
        user.password
    )

    if existing_user is None:
        return {
            "error": "Invalid credentials"
        }

    access_token = create_access_token(
        data={
            "sub": existing_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }