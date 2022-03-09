from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter

from .models import Genre, Person, FilmWork, GenreFilmWork, PersonFilmWork


class GenreFilmWorkInline(admin.TabularInline):
    model = GenreFilmWork


class PersonFilmWorkInline(admin.TabularInline):
    model = PersonFilmWork


@admin.register(FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmWorkInline, PersonFilmWorkInline)
    list_display = ('title', 'type', 'creation_date', 'rating')
    search_fields = ('title', 'description')
    list_filter = (
        'type',
        ('rating', DropdownFilter)
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
