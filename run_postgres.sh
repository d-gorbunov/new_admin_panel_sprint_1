docker run -d --rm \
    --name postgres \
    -p 5432:5432 \
    -v ${HOME}/postgresql/data:/var/lib/postgresql/data \
    -e POSTGRES_DB=${DB_NAME} \
    -e POSTGRES_USER=${DB_USER} \
    -e POSTGRES_PASSWORD=${DB_PASSWORD} \
    postgres:13
