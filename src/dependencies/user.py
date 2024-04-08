from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from constants.group_model import ADMINISTRATOR_GROUP_NAME
from database import SessionLocal
from helpers.token import get_current_user as get_current_user_from_token
from models.user import User as UserModel
from services.group import get_or_create_group

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """FastAPI Depend for getting current user from oauth2_scheme token

    Args:
        token (Annotated[str, Depends): token auth from oauth2_scheme

    Raises:
        credentials_exception: Token is invalid or expired
        credentials_exception: User does not exist

    Returns:
        UserModel: Current user
    """

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        headers={"WWW-Authenticate": "Bearer"},
    )

    db = SessionLocal()

    try:
        user = get_current_user_from_token(db=db, token=token)
    except JWTError as jwt_error:
        credentials_exception.detail = str(jwt_error)
        raise credentials_exception from jwt_error

    if user is None:
        credentials_exception.detail = 'User does not exist'
        raise credentials_exception

    return user


async def get_current_superuser(current_user: Annotated[UserModel, Depends(get_current_user)]):
    db = SessionLocal()
    admin_group = get_or_create_group(db, name=ADMINISTRATOR_GROUP_NAME)
    if current_user.group is None or current_user.group.id != admin_group.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not administrator")
    return current_user
