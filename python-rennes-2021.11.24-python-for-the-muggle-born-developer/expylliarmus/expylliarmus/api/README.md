
# Launch the web application locally

```sh
# starts the web server with a specific HTTP port (8080 by default)
bash start-expylliarmus-server.sh -h 8888

# starts the web server with 2 workers
bash start-expylliarmus-server.sh -w 2

# starts the web server in reload mode (restarts the web server when developing)
bash start-expylliarmus-server.sh -r

# specifies where the reference datasets should be read (local/books by default)
bash start-expylliarmus-server.sh -b "local/books"
```

# Endpoints
## POSTs books to the web API

```sh
curl -X POST "http://localhost:8080/books/upload" -F "file=@$(pwd)/tests/data/3-azkaban.txt"
```

## GETs the uploaded book file names

```sh
curl -X GET "http://localhost:8080/books"
```

## Analyzes the spells for a POSTed book id (the file name without '.txt')

```sh
curl -X POST "http://localhost:8080/books/3-azkaban/analyze-spells"
```

# Builds and runs the Docker container

```sh
# builds the expylliarmus:local image
docker build --build-arg PYTHON_VERSION=$(cat .python-version) --tag expylliarmus:local --file Dockerfile .

# runs the image in the auto-remove mode
docker run --rm -p 8080:8080 -t expylliarmus:local

# stops the container (and auto-removes it)
docker stop $(docker ps -a -q --filter ancestor=expylliarmus:local --format="{{.ID}}")
```
