#!/bin/sh

HTTP_PORT='8080'
WORKERS=''
RELOAD=''
while getopts h:w:b:r OPTION "$@"; do
    # echo "option ${OPTION}"
    case $OPTION in
        # HTTP port
        h)
            HTTP_PORT=${OPTARG}
            ;;
        # number of workers
        w)
            WORKERS="--workers ${OPTARG}"
            ;;
        # path to the folder containing the books (absolute or relative), envvar read by the application
        b)
            EXP_BOOKS_FOLDER=${OPTARG}
            ;;
        # starts the application in development mode (reload server on *.py changes)
        r)
            RELOAD='--reload'
            ;;
        \?)
            echo "Invalid option: $OPTION" 1>&2
            ;;
    esac
done

echo "$(date '+%Y-%m-%d_%H:%M:%S') Starting expylliarmus server on HTTP_PORT ${HTTP_PORT}, WORKERS ${WORKERS}, RELOAD ${RELOAD}"

poetry run uvicorn expylliarmus.api.__main__:expylliarmus --host 0.0.0.0 --port "${HTTP_PORT}" ${WORKERS} ${RELOAD}
