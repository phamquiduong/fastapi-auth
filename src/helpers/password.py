from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str):
    """Verify password

    Args:
        plain_password (str): Plain password
        hashed_password (str): Hash of the password

    Returns:
        bool: Is the plain password and the hashed password correct
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    """Get password hash string from password plain text

    Args:
        password (str): Password plain text

    Returns:
        str: Hashed password
    """
    return pwd_context.hash(password)
