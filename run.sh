##!/bin/bash

#Check if the activate script exists
if [ -f "./.venv/bin/activate" ]; then
    source "./.venv/bin/activate"
else
    echo "Virtual environment does not exist. Creating virtual environment"
    python3 -m venv .venv
    source "./.venv/bin/activate"
fi

echo "Checking Dependancies"
#Sudo dependecies for some reason, to find out why
pip install -r requirements.txt >/dev/null

#Check if database has been generated
if [ ! -f "./.sql_app.db" ]; then
    echo "Database file does not exist. Creating database."
    alembic upgrade head

echo "Running Server"
uvicorn app.main:app --reload 
