\c movies

CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.film_work (
    id UUID PRIMARY KEY NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT,
    type VARCHAR(10) NOT NULL,
    created TIMESTAMP WITH TIME ZONE,
    modified TIMESTAMP WITH TIME ZONE
);

CREATE TABLE IF NOT EXISTS content.genre (
    id UUID PRIMARY KEY NOT NULL,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created TIMESTAMP WITH TIME ZONE,
    modified TIMESTAMP WITH TIME ZONE
);

CREATE TABLE IF NOT EXISTS content.person (
    id UUID PRIMARY KEY NOT NULL,
    full_name VARCHAR(50) NOT NULL,
    created TIMESTAMP WITH TIME ZONE,
    modified TIMESTAMP WITH TIME ZONE
);

CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id UUID PRIMARY KEY NOT NULL,
    genre_id UUID NOT NULL REFERENCES content.genre(id) ON DELETE CASCADE,
    film_work_id UUID NOT NULL REFERENCES content.film_work(id) ON DELETE CASCADE,
    created TIMESTAMP WITH TIME ZONE
);

CREATE TABLE IF NOT EXISTS content.person_film_work (
    id UUID PRIMARY KEY NOT NULL,
    person_id UUID NOT NULL REFERENCES content.person(id) ON DELETE CASCADE,
    film_work_id UUID NOT NULL REFERENCES content.film_work(id) ON DELETE CASCADE,
    role VARCHAR(50) NOT NULL,
    created TIMESTAMP WITH TIME ZONE
);

CREATE INDEX IF NOT EXISTS film_work_title_idx ON content.film_work(title);
CREATE UNIQUE INDEX IF NOT EXISTS genre_film_work_idx ON content.genre_film_work(genre_id, film_work_id);
CREATE INDEX IF NOT EXISTS film_work_creation_date_rating_idx ON content.film_work(creation_date, rating);
CREATE UNIQUE INDEX IF NOT EXISTS person_film_work_idx ON content.person_film_work(person_id, film_work_id);
