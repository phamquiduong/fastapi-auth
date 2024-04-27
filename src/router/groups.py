from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm import Session

from constants.query import QUERY_LIMIT
from dependencies.db import get_db
from dependencies.user import get_current_superuser
from models import User as UserModel
from schemas import ErrorSchema, Group, User
from services.group import get_groups
from services.user import get_users

router = APIRouter(prefix='/groups', tags=['Groups'])


@router.get('', response_model=list[Group],
            responses={401: {'model': ErrorSchema},
                       404: {'model': ErrorSchema},
                       403: {'model': ErrorSchema},
                       422: {'model': ErrorSchema},
                       500: {'model': ErrorSchema},
                       })
def get_groups_list(
    _: Annotated[UserModel, Depends(get_current_superuser)],
    skip: int = Query(0),
    limit: int = Query(QUERY_LIMIT),
    db: Session = Depends(get_db)
):
    return get_groups(db, skip, limit)


@router.get('/{group_id}/users', response_model=list[User],
            responses={401: {'model': ErrorSchema},
                       404: {'model': ErrorSchema},
                       403: {'model': ErrorSchema},
                       422: {'model': ErrorSchema},
                       500: {'model': ErrorSchema},
                       })
def get_group_users(
    _: Annotated[UserModel, Depends(get_current_superuser)],
    group_id: int = Path(...),
    skip: int = Query(0),
    limit: int = Query(QUERY_LIMIT),
    db: Session = Depends(get_db)
):
    return get_users(db, skip, limit, group_id=group_id)
