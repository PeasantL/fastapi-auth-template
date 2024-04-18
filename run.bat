@echo off

REM Check if the activate script exists
IF EXIST ".\.venv\Scripts\activate.bat" (
    CALL ".\.venv\Scripts\activate.bat"
) ELSE (
    echo Virtual environment does not exist. Creating virtual environment
    python -m venv .venv
    CALL ".\.venv\Scripts\activate.bat"
)

echo Checking Dependencies
REM Installing dependencies, ensure pip is up to date
REM Silence output unless there are errors
pip install -r requirements.txt >NUL

REM Check if database exists
IF NOT EXIST ".\sql_app.db" (
    echo Database file does not exist. Creating database.
    CALL alembic upgrade head
)

echo Running Server
REM Start the server
uvicorn app.main:app --reload
