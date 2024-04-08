from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from constants.group_model import ADMINISTRATOR_GROUP_NAME
from constants.query import QUERY_LIMIT
from dependencies.db import get_db
from dependencies.user import get_current_superuser, get_current_user
from schemas import User
from services.group import get_or_create_group
from services.user import get_user, get_users

router = APIRouter(prefix='/users', tags=['Users'])


@router.get('', response_model=list[User])
def get_user_list(
    _: Annotated[User, Depends(get_current_superuser)],
    skip: int = Query(0),
    limit: int = Query(QUERY_LIMIT),
    db: Session = Depends(get_db)
):
    return get_users(db, skip=skip, limit=limit)


@router.get('/me', response_model=User)
def get_current_user_info(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return User(
        id=current_user.id,
        email=current_user.email,
        group=current_user.group
    )


@router.get('/{user_id}', response_model=User)
def get_user_info_by_id(
    current_user: Annotated[User, Depends(get_current_user)],
    user_id: int,
    db: Session = Depends(get_db)
):
    admin_group = get_or_create_group(db, name=ADMINISTRATOR_GROUP_NAME)
    if current_user.id != user_id and (current_user.group is None or current_user.group.id != admin_group.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You cannot get other user information when you are not an admin."
        )

    user_db = get_user(db, user_id=user_id)

    if user_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id {user_id} does not exist'
        )

    return User(
        id=user_db.id,          # type:ignore
        email=user_db.email,    # type:ignore
        group=user_db.group
    )
