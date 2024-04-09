from typing import Annotated

from fastapi import APIRouter, Body, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from dependencies.db import get_db
from errors.auth import AuthError
from helpers.token import create_access_token
from schemas import User, UserCreate, UserLogin
from schemas.token import Token
from services.user import authenticate_user, create_superuser, create_user, get_user_by_email, is_exists_user

router = APIRouter(prefix='/auth', tags=['Authentication'])


@router.post("/token", response_model=Token, include_in_schema=False)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    access_token = create_access_token(user)
    return Token(access_token=access_token, token_type="bearer")


@router.post('/register', response_model=User, status_code=status.HTTP_201_CREATED)
def register(
    user_create: UserCreate,
    db: Session = Depends(get_db)
):
    if get_user_by_email(db, email=user_create.email) is not None:
        raise AuthError.AUTH_409_001.value

    user_db = create_user(db, user_create) if is_exists_user(db) else create_superuser(db, user_create)
    return User(
        id=user_db.id,          # type:ignore
        email=user_db.email,    # type:ignore
        group=user_db.group
    )


@router.post("/login", response_model=Token)
async def login(
    user_login: UserLogin = Body(...),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, user_login.email, user_login.password)
    access_token = create_access_token(user)
    return Token(access_token=access_token, token_type="bearer")
