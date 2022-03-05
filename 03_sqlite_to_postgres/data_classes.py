import uuid
from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class Common:
    __slots__ = ('id', 'created', 'modified')
    id: uuid.UUID
    created: datetime
    modified: datetime


@dataclass(frozen=True)
class FilmWork(Common):
    __slots__ = ('title', 'description', 'creation_date', 'rating', 'type')
    type: str
    title: str
    rating: float
    description: str
    creation_date: datetime


@dataclass(frozen=True)
class Genre(Common):
    __slots__ = ('name', 'description')
    name: str
    description: str


@dataclass(frozen=True)
class Person(Common):
    __slots__ = ('full_name',)
    full_name: str


@dataclass(frozen=True)
class GenreFilmWork(Common):
    __slots__ = ('genre_id', 'film_work_id')
    genre_id: uuid.UUID
    film_work_id: uuid.UUID


@dataclass(frozen=True)
class PersonFilmWork(Common):
    __slots__ = ('role', 'person_id', 'film_work_id')
    role: str
    person_id: uuid.UUID
    film_work_id: uuid.UUID
