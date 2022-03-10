import uuid
from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class Common:
    id: uuid.UUID
    created_at: datetime


@dataclass(frozen=True)
class FilmWork(Common):
    __slots__ = ('id', 'title', 'description', 'creation_date', 'rating', 'type', 'created_at', 'updated_at')
    type: str
    title: str
    rating: float
    description: str
    updated_at: datetime
    creation_date: datetime


@dataclass(frozen=True)
class Genre(Common):
    __slots__ = ('id', 'name', 'description', 'created_at', 'updated_at')
    name: str
    description: str
    updated_at: datetime


@dataclass(frozen=True)
class Person(Common):
    __slots__ = ('id', 'full_name', 'created_at', 'updated_at')
    full_name: str
    updated_at: datetime


@dataclass(frozen=True)
class GenreFilmWork(Common):
    __slots__ = ('id', 'genre_id', 'film_work_id', 'created_at')
    genre_id: uuid.UUID
    film_work_id: uuid.UUID


@dataclass(frozen=True)
class PersonFilmWork(Common):
    __slots__ = ('id', 'person_id', 'film_work_id', 'role', 'created_at')
    role: str
    person_id: uuid.UUID
    film_work_id: uuid.UUID
