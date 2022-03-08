import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PersonRoleChoices(models.TextChoices):
    actor = 'Actor'
    writer = 'Writer'
    director = 'Director'


class FilmWorkTypeChoices(models.TextChoices):
    tv_show = 'TV Show'
    movie = 'Movie'


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField('name', max_length=50)
    description = models.TextField('description', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = 'genre'
        verbose_name_plural = 'genres'


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField('full_name', max_length=50)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "content\".\"person"
        verbose_name = 'person'
        verbose_name_plural = 'persons'


class PersonFilmWork(UUIDMixin):
    film_work_id = models.ForeignKey('FilmWork', on_delete=models.CASCADE)
    person_id = models.ForeignKey('Person', on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=PersonRoleChoices.choices)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "content\".\"person_film_work"


class GenreFilmWork(UUIDMixin):
    genre_id = models.ForeignKey('Genre', on_delete=models.CASCADE)
    film_work_id = models.ForeignKey('FilmWork', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "content\".\"genre_film_work"


class FilmWork(UUIDMixin, TimeStampedMixin):
    title = models.CharField('title', max_length=255)
    description = models.TextField('description', blank=True)
    creation_date = models.DateField('creation_date', blank=True)
    rating = models.FloatField('rating', blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    type = models.CharField('type', max_length=10, choices=FilmWorkTypeChoices.choices)
    genres = models.ManyToManyField(Genre, through='GenreFilmWork')
    persons = models.ManyToManyField(Person, through='PersonFilmWork')

    def __str__(self):
        return self.title

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = 'movie'
        verbose_name_plural = 'movies'
