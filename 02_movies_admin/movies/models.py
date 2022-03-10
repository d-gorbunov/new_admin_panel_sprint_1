import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PersonRoleChoices(models.TextChoices):
    actor = _('Actor')
    writer = _('Writer')
    director = _('Director')


class FilmWorkTypeChoices(models.TextChoices):
    tv_show = _('TV Show')
    movie = _('Movie')


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_('name'), max_length=50)
    description = models.TextField(_('description'), blank=True)

    def __str__(self) -> models.CharField:
        return self.name

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = _('genre')
        verbose_name_plural = _('genres')


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(_('full_name'), max_length=50)

    def __str__(self) -> models.CharField:
        return self.full_name

    class Meta:
        db_table = "content\".\"person"
        verbose_name = _('person')
        verbose_name_plural = _('persons')


class PersonFilmWork(UUIDMixin):
    film_work = models.ForeignKey('FilmWork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    role = models.CharField(_('role'), max_length=50, choices=PersonRoleChoices.choices)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"
        constraints = [
            models.UniqueConstraint(fields=['film_work', 'person', 'role'], name='unique_movie_person_role')
        ]


class GenreFilmWork(UUIDMixin):
    film_work = models.ForeignKey('FilmWork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        constraints = [
            models.UniqueConstraint(fields=['film_work', 'genre'], name='unique_movie_genre')
        ]


class FilmWork(UUIDMixin, TimeStampedMixin):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    creation_date = models.DateField(_('creation_date'), blank=True)
    rating = models.FloatField(_('rating'), blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    type = models.CharField(_('type'), max_length=10, choices=FilmWorkTypeChoices.choices)
    genres = models.ManyToManyField(Genre, through='GenreFilmWork')
    persons = models.ManyToManyField(Person, through='PersonFilmWork')

    def __str__(self) -> models.CharField:
        return self.title

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = _('movie')
        verbose_name_plural = _('movies')
        indexes = [
            models.Index(fields=['title'], name='film_work_title_idx'),
            models.Index(fields=['creation_date', 'rating'], name='movie_release_date_rating_idx')
        ]
