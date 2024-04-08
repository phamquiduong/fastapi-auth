from sqlalchemy.orm import Session

from models import Group as GroupModel


def get_group(db: Session, group_id: int):
    """Get group by id

    Args:
        db (Session): Database session
        group_id (int): Group id

    Returns:
        GroupModel: Group By Id provided
    """
    return db.query(GroupModel).filter(GroupModel.id == group_id).first()


def get_group_by_name(db: Session, name: str):
    """Get group by name

    Args:
        db (Session): Database session
        name (str): Group name

    Returns:
        GroupModel: Group by Name provided
    """
    return db.query(GroupModel).filter(GroupModel.name == name).first()


def create_group(db: Session, name: str):
    """Create a new group by name

    Args:
        db (Session): Database session
        name (str): Group name

    Returns:
        GroupModel: Group created
    """
    group_db = GroupModel(name=name)
    db.add(group_db)
    db.commit()
    db.refresh(group_db)
    return group_db


def get_or_create_group(db: Session, name: str):
    """Get or create group if group with name does not exist

    Args:
        db (Session): Database session
        name (str): Group name

    Returns:
        GroupModel: Group model
    """
    group = get_group_by_name(db, name)
    if group is None:
        group = create_group(db, name)
    return group
