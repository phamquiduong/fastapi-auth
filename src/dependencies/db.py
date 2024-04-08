from database import SessionLocal


def get_db():
    """ FastAPI Depend for get the database session.

    Yields:
        Session: The database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
