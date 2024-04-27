from models.user import User as UserModel
from typing import Annotated
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from constants.query import QUERY_LIMIT
from dependencies.db import get_db
from dependencies.user import get_current_superuser
from schemas import Group
from services.group import get_groups

router = APIRouter(prefix='/groups', tags=['Groups'])


@router.get('', response_model=list[Group])
def get_groups_list(
    _: Annotated[UserModel, Depends(get_current_superuser)],
    skip: int = Query(0),
    limit: int = Query(QUERY_LIMIT),
    db: Session = Depends(get_db)
):
    return get_groups(db, skip, limit)
