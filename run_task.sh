#!/bin/bash

cd $(dirname $0)

REPOSITORY_DIR="$PWD"

INPUT_DATA=""
LANGUAGE="python"

while getopts "t:l:i" option ; do
    case "$option" in
      "t") TASK_NAME=$OPTARG ;;

      "i") read INPUT_DATA ;;
      
      "l") 
            if [[ "$OPTARG" == "r" ]]; then
                  LANGUAGE="R"
            fi

            if [[ "$OPTARG" == "Py*" ]] || [[ "$OPTARG" == "py*" ]]; then
                  LANGUAGE="python"
            fi ;;

      *) exit 0 ;;
    esac
done


TASK_NAME=$(echo $TASK_NAME | tr '[:lower:]' '[:upper:]')
FULL_PATH="$REPOSITORY_DIR/$TASK_NAME"

if [[ ! -d $FULL_PATH ]]; then
    echo -e "Folder $TASK_NAME didnt exist.\tTerminating running script"
    exit 0
fi

###########################################################

# make -C $TASK_NAME
# echo "python3 $TASK_NAME << $INPUT_DATA | $LANGUAGE"

echo "lang is $LANGUAGE"

case "$INPUT_DATA" in
      "") make -C $TASK_NAME "test_$LANGUAGE" ;;

      *)  make -C $TASK_NAME "own_input_$LANGUAGE" INPUT_DATA="$INPUT_DATA" ;;
esac
