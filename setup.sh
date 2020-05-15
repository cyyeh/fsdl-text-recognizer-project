#!/bin/bash
# in order to execute python script of the project
export PYTHONPATH=.
# create a jupyter notebook kernel that has the same computing environment 
# as the virtual environment of the project
export KERNEL_NAME="my-kernel"
export DISPLAY_NAME="fsdl-text-recognizer"
pipenv install ipykernel --dev
pipenv run python -m ipykernel install --name $KERNEL_NAME --display-name "$DISPLAY_NAME" --user