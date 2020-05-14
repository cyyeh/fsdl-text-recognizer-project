export KERNEL_NAME="my-kernel"
export DISPLAY_NAME="fsdl-text-recognizer"
pipenv install ipykernel --dev
pipenv run python -m ipykernel install --name $KERNEL_NAME --display-name "$DISPLAY_NAME" --user