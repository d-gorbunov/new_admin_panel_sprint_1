import sqlite3
from contextlib import contextmanager
from collections.abc import Generator

import psycopg2
from psycopg2 import OperationalError
from psycopg2.extensions import connection as _connection


@contextmanager
def sqlite_connector(db_path: str) -> Generator[sqlite3.Connection, None, None]:
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    except sqlite3.Error as exc:
        raise exc
    finally:
        conn.close()


@contextmanager
def postgres_connector(dsn: dict[str, str]) -> Generator[_connection, None, None]:
    conn = psycopg2.connect(**dsn)
    try:
        yield conn
    except OperationalError as exc:
        raise exc
    finally:
        conn.close()
