from datetime import timedelta
from pathlib import Path

# App Config
APP_TITLE = 'FastAPI Authentication Application'
APP_VERSION = '1.0.0'

# Using SQLite database. Path ../db.sqlite
SQLALCHEMY_DATABASE_URL = "sqlite:///../database/db.sqlite"

# Secret key for JWT.
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

# Algorithm for JWT.
ALGORITHM = "HS256"

# Expiration time for JWT (1day)
ACCESS_TOKEN_EXPIRE = timedelta(days=1)

# Current directory
BASE_DIR = Path(__file__).resolve().parent

# Logging configuration
LOG_DIR = BASE_DIR / '../log'
LOG_LEVEL = 'DEBUG'
LOG_FORMAT = '[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s'
LOG_TIME_FORMAT = '%y-%m-%d %H:%M:%S'
LOG_HANDLERS = ['console', 'file']
