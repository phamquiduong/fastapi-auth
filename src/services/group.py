from sqlalchemy.orm import Session

from models import Group as GroupModel


def get_group(db: Session, group_id: int):
    return db.query(GroupModel).filter(GroupModel.id == group_id).first()


def get_group_by_name(db: Session, name: str):
    return db.query(GroupModel).filter(GroupModel.name == name).first()


def create_group(db: Session, name: str):
    group_db = GroupModel(name=name)
    db.add(group_db)
    db.commit()
    db.refresh(group_db)
    return group_db


def get_or_create_group(db: Session, name: str):
    group = get_group_by_name(db, name)
    if group is None:
        group = create_group(db, name)
    return group
