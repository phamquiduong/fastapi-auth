@echo off
REM Install all python packages
pip install -r requirements.txt

REM Change directory to the "src" folder
cd /d "src"

REM Read the port number from the user (with default value 80)
set /p PORT=Enter the port number (default is 80):

REM Check if PORT variable is empty (default value)
if "%PORT%"=="" set PORT=80

REM Run the FastAPI app using uvicorn, checking for PORT value
uvicorn main:app --host 0.0.0.0 --port %PORT% --reload
