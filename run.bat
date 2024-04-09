@echo off
REM Install all python packages
pip install -r requirements.txt


REM Run all migration tasks
mkdir database
alembic upgrade head


REM Change directory to the "src" folder
cd /d "src"


REM Copy config file when config file does not exist
if not exist config.py (
    copy config.example.py config.py
    echo config.py copied successfully.
) else (
    echo config.py already exists.
)


REM Read the port number from the user (with default value 80)
set /p PORT=Enter the port number (default is 80):


REM Check if PORT variable is empty (default value)
if "%PORT%"=="" set PORT=80


REM Run the FastAPI app using uvicorn, checking for PORT value
uvicorn main:app --host 0.0.0.0 --port %PORT% --reload
