#! /bin/bash

cd $(dirname $0)

REPOSITORY_DIR="$PWD"
TASK_NAME="$1"

if [ -z $1 ]; then
    echo "Expected to receive task name:"
    read TASK_NAME
fi

TASK_NAME=$(echo $TASK_NAME | tr '[:lower:]' '[:upper:]')
FULL_PATH="$REPOSITORY_DIR/$TASK_NAME"

if [[ ! -d $FULL_PATH ]]; then
    echo -e "Folder $TASK_NAME didnt exist.\tTerminating running script"
    exit 0
fi

make -C $TASK_NAME