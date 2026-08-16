import pytest

from src.database.connection import create_engine
from src.database.repositories.movie_repository import MovieRepository


@pytest.fixture
def repository():
    engine = create_engine()
    
    with engine.connect() as conn:
        yield MovieRepository(conn)


def test_get_all_movies(repository):
    movies = repository.get_all_movies()

    assert not movies.empty
    assert {"id", "title", "year"} <= set(movies.columns)


def test_get_movie_by_id(repository):
    movie = repository.get_movie_by_id(1)

    assert not movie.empty
    assert {"id", "title", "year"} <= set(movie.columns)
    assert movie.iloc[0]["id"] == 1


def test_get_movies_by_ids(repository):
    movies = repository.get_movies_by_ids([1, 2, 3])

    assert not movies.empty
    assert {"id", "title", "year"} <= set(movies.columns)


def test_get_movie_genres(repository):
    genres = repository.get_movie_genres(1)

    assert not genres.empty
    assert {"id", "name"} <= set(genres.columns)