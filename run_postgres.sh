docker run --rm -d \
    --name postgres \
    -p 5432:5432 \
    -v ${HOME}/postgresql/data:/var/lib/postgresql/data \
    -e POSTGRES_USER=${POSTGRES_USER} \
    -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
    postgres:13
