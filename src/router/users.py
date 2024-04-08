from typing import Annotated

from fastapi import APIRouter, Depends

from dependencies.user import get_current_user
from schemas import User

router = APIRouter(prefix='/users', tags=['Users'])


@router.get('/me', response_model=User)
def get_current_user_info(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return User(
        email=current_user.email,
        group=current_user.group
    )
