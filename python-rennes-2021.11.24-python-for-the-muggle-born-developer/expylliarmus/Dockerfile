
ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}-slim

# do not buffer python output at all
ENV PYTHONUNBUFFERED=1 \
    # do not write `__pycache__` bytecode
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry install folder
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's folder as `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    VENV_PATH="/opt/pysetup/.venv"

# adds poetry to the path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# where the books to store and to analyze are located
RUN mkdir -p /expylliarmus/books
ENV EXP_BOOKS_FOLDER="/expylliarmus/books"

# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN apt-get update && apt-get install --no-install-recommends -y curl
ARG POETRY_VERSION=1.1.11
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
# production installation
WORKDIR /expylliarmus
COPY ./poetry.lock ./pyproject.toml ./poetry.toml ./start-expylliarmus-server.sh ./
RUN poetry install --no-dev
COPY ./expylliarmus ./expylliarmus/

EXPOSE 8080
ENTRYPOINT ["/expylliarmus/start-expylliarmus-server.sh"]
CMD ["-b", "/expylliarmus/books"]
