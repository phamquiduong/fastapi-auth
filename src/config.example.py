from datetime import timedelta

# Using SQLite database. Path ../db.sqlite
SQLALCHEMY_DATABASE_URL = "sqlite:///../db.sqlite"

# Secret key for JWT.
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

# Algorithm for JWT.
ALGORITHM = "HS256"

# Expiration time for JWT (1day)
ACCESS_TOKEN_EXPIRE = timedelta(days=1)
