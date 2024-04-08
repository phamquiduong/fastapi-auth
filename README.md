# FastAPI Authentication
> FastAPI Authentication custom

<br>

# Development
Program language | Framework | Database | Migrations
--- | --- | --- | ---
Python 3.11 <br> [Official Website](https://www.python.org/downloads/release/python-3118/) <br> [Microsoft Store](https://apps.microsoft.com/detail/9nrwmjp3717k?hl=en-us&gl=US) <br> [Brew](https://formulae.brew.sh/formula/python@3.11) | [FastAPI](https://fastapi.tiangolo.com/) | SQLite3 | [Alembic](https://alembic.sqlalchemy.org/en/latest/)

<br>

# Build server
### Install the python package
```bash
pip install -r requirements.txt
```

### Run migrations
```bash
alembic upgrade head
```

<br>

# Run server
### Change the directory to src folder
```bash
cd src
```

### Run server
```bash
uvicorn main:app
```
> **Note:**
> * Add flag `--reload` to reload the server after change code
> * Add flag `--port` to setup port number. Example: `--port 80`


<br>

# Project tree
```bash
fastapi-auth
└─ src
   ├─ dependencies      # Dependencies
   ├─ helpers           # Python Helpers
   ├─ models            # Project Models
   ├─ router            # APIRouter
   ├─ schemas           # Schemas
   ├─ services          # Services
   ├─ config.py         # Config/ Constants for project
   ├─ database.py       # Database connection
   └─ main.py           # Project root
```
