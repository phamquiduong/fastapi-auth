# FastAPI Authentication
> FastAPI Authentication customizer by [phamquiduong](https://github.com/phamquiduong)

<br>

# Development
Program language | Framework | Database | Migrations
--- | --- | --- | ---
Python 3.11 <br> [Official Website](https://www.python.org/downloads/release/python-3118/) <br> [Microsoft Store](https://apps.microsoft.com/detail/9nrwmjp3717k?hl=en-us&gl=US) <br> [MacOS Brew](https://formulae.brew.sh/formula/python@3.11) | [FastAPI](https://fastapi.tiangolo.com/) | SQLite3 | [Alembic](https://alembic.sqlalchemy.org/en/latest/)

<br>

# Build and run server
### Method 1: Using Windows Batch file
> * In windows OS, run `run.bat` file for automatic build and run server
>   ```bash
>   .\run.bat
>   ```

### Method 2: Using Docker
> * Change directory to src folder
>   ```bash
>   cd src
>   ```
> * Copy config.example.py to config.py file
>   ```bash
>   cp config.example.py config.py
>   ```

> * Change directory to docker folder
>   ```bash
>   cd ../docker
>   ```
> * Copy .env.example to .env file
>   ```bash
>   cp .env.example .env
>   ```
> * Create network
>   ```bash
>   docker network create fast_api_auth_network
>   ```

> * Build docker compose command
>   ```bash
>   docker-compose build
>   ```
> * Up docker compose command
>   ```bash
>   docker-compose up --d
>   ```

### Method 3: Manual build and run server
> * Install the python package
>   ```bash
>   pip install -r requirements.txt
>   ```

> * Create database folder
>   ```bash
>   mkdir database
>   ```
> * Run migrations
>   ```bash
>   alembic upgrade head
>   ```

> * Change directory to src folder
>   ```bash
>   cd src
>   ```
> * Create config.py file
>   ```bash
>   cp config.example.py config.py
>   ```
> * Run server
>   ```bash
>   uvicorn main:app
>   ```
>   **Note:**
>   * Add flag `--reload` to reload the server after change code
>   * Add flag `--port` to setup port number. Example: `--port 80`

<br>

# Project tree
```bash
fastapi-auth
├─ database             # Sqlite Database folder
├─ docker               # Docker folder
├─ migrations           # Alembic migration folder
├─ alembic.ini          # Alembic configuration
├─ run.bat              # Windows one click to run batch
├─ requirements.txt     # Python package requirements file
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
