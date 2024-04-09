from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose.exceptions import ExpiredSignatureError, JWTError

from constants.group_model import ADMINISTRATOR_GROUP_NAME
from database import SessionLocal
from errors.auth import AuthError
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
    db = SessionLocal()

    try:
        user = get_current_user_from_token(db=db, token=token)
    except ExpiredSignatureError as expired_signature_error:
        raise AuthError.AUTH_401_001.value from expired_signature_error
    except JWTError as jwt_error:
        raise AuthError.AUTH_401_002.value from jwt_error

    if user is None:
        raise AuthError.AUTH_404_001.value

    return user


async def get_current_superuser(current_user: Annotated[UserModel, Depends(get_current_user)]):
    """FastAPI Depend for getting current superuser

    Args:
        current_user (Annotated[UserModel, Depends): User logined

    Raises:
        AuthError.AUTH_403_001.value: User are not administrator

    Returns:
        UserModel: Current superuser
    """
    db = SessionLocal()
    admin_group = get_or_create_group(db, name=ADMINISTRATOR_GROUP_NAME)
    if current_user.group is None or current_user.group.id != admin_group.id:
        raise AuthError.AUTH_403_001.value
    return current_user
