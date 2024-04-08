from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from database import SessionLocal
from helpers.token import get_current_user as get_current_user_from_token

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
