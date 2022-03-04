docker run --rm -d \
    --name postgres \
    -p 5432:5432 \
    -v ${HOME}/postgresql/data:/var/lib/postgresql/data \
    -e DB_USER=${DB_USER} \
    -e DB_PASSWORD=${DB_PASSWORD} \
    postgres:13
