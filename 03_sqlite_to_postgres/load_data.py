import os
import csv
import sqlite3
import tempfile

import psycopg2
from psycopg2.extras import DictCursor
from psycopg2 import DatabaseError, OperationalError
from psycopg2.extensions import connection as _connection

from data_classes import FilmWork, Genre, Person, GenreFilmWork, PersonFilmWork

tables_map = {
    'genre': Genre,
    'person': Person,
    'film_work': FilmWork,
    'genre_film_work': GenreFilmWork,
    'person_film_work': PersonFilmWork
}

BATCH_SIZE = 5000


class PostgresSaver:
    def __init__(self, connection):
        self._connection = connection

    def save_all_data(self, data):
        pass


class SQLiteLoader:
    def __init__(self, connection):
        self._connection = connection

    def load_movies(self):
        cursor = self._connection.cursor()
        for table, class_ in tables_map.items():
            file_path = os.path.abspath(os.path.join(tempfile.gettempdir(), f'{table}.csv'))
            try:
                with open(file_path, 'w', encoding='utf-8', newline='') as f:
                    fieldnames = class_.__slots__
                    writer = csv.DictWriter(f, fieldnames)
                    writer.writeheader()
                    cursor.execute('SELECT {columns} FROM {table}'.format(columns=', '.join(fieldnames), table=table))
                    while True:
                        data = cursor.fetchmany(size=BATCH_SIZE)
                        if not data:
                            break
                        print(data)
            except IOError as e:
                print(f'ERROR! Can\'t handle with file: {e.filename}.\nREASON: {e.strerror}')


        cursor.close()


def load_from_sqlite(sqlite_connection: sqlite3.Connection, postgres_connection: _connection) -> None:
    """ Основной метод загрузки данных из SQLite в Postgres """
    postgres_saver = PostgresSaver(postgres_connection)
    sqlite_loader = SQLiteLoader(sqlite_connection)

    data = sqlite_loader.load_movies()
    postgres_saver.save_all_data(data)


if __name__ == '__main__':
    dsn = {
        'dbname': os.environ.get('DB_NAME'),
        'user': os.environ.get('DB_USER'),
        'password': os.environ.get('DB_PASSWORD'),
        'host': os.environ.get('DB_HOST', '127.0.0.1'),
        'port': os.environ.get('DB_PORT', 5432)
    }
    pg_conn, sqlite_conn = None, None
    try:
        with sqlite3.connect('db.sqlite') as sqlite_conn, psycopg2.connect(**dsn, cursor_factory=DictCursor) as pg_conn:
            load_from_sqlite(sqlite_conn, pg_conn)
    except (DatabaseError, OperationalError) as exc:
        print(f'ERROR! Can\'t handle with database.\nREASON: {exc}')
    finally:
        if pg_conn:
            pg_conn.close()

        if sqlite_conn:
            sqlite_conn.close()
