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
pip sudo install -r requirements.txt
echo "Running Server"


uvicorn main:app --reload 
