from sqlalchemy.orm import Session

from constants.group_model import ADMINISTRATOR_GROUP_NAME
from constants.query import QUERY_LIMIT
from errors.auth import AuthError
from helpers.password import get_password_hash, verify_password
from models import User as UserModel
from schemas import UserCreate
from services.group import get_or_create_group


def get_user(db: Session, user_id: int):
    """Get user by user id

    Args:
        db (Session): Database session
        email (str): User id

    Returns:
        UserModel: current user
    """
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """Get user by email

    Args:
        db (Session): Database session
        email (str): User email

    Returns:
        UserModel: current user
    """
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = QUERY_LIMIT):
    """Get list of users

    Args:
        db (Session): Database session
        skip (int, optional): Skip. Defaults to 0.
        limit (int, optional): Limit. Defaults to constants.query.QUERY_LIMIT.

    Returns:
        list[UserModel]: List of users
    """
    return db.query(UserModel).offset(skip).limit(limit).all()


def is_exists_user(db: Session):
    """Check if anyone exists in the database?

    Args:
        db (Session): Database session

    Returns:
        bool: Is anyone exists
    """
    return db.query(UserModel).first() is not None


def create_user(db: Session, user_create: UserCreate):
    """Create a users

    Args:
        db (Session): Database session
        user_create (UserCreate): User Create schema

    Returns:
        UserModel: user created
    """
    password = get_password_hash(user_create.password)
    user_db = UserModel(email=user_create.email, password=password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db


def create_superuser(db: Session, user_create: UserCreate):
    """Create a superuser

    Args:
        db (Session): Database session
        user_create (UserCreate): User Create schema

    Returns:
        UserModel: superuser created
    """
    user_db = create_user(db, user_create)
    admin_group = get_or_create_group(db, name=ADMINISTRATOR_GROUP_NAME)
    user_db.group = admin_group
    db.commit()
    db.refresh(user_db)
    return user_db


def authenticate_user(db: Session, email: str, password: str):
    """Authenticate a user

    Args:
        db (Session): Database session
        email (str): User email
        password (str): User password

    Raises:
        authenticate_exception: Email does not exist
        authenticate_exception: Password is incorrect

    Returns:
        UserModel: current user authenticated
    """
    user_db = get_user_by_email(db, email)

    if user_db is None:
        raise AuthError.AUTH_400_001.value

    if not verify_password(plain_password=password, hashed_password=user_db.password):  # type: ignore
        raise AuthError.AUTH_400_002.value

    return user_db
