import pytest

from src.database.repositories.movie_repository import MovieRepository
from src.database.session import SessionLocal
from src.models.genre import Genre
from src.models.movie import Movie


@pytest.fixture
def repository():
    with SessionLocal() as session:
        yield MovieRepository(session)


def test_get_all(repository):
    movies = repository.get_all()

    assert len(movies) > 0
    assert all(isinstance(movie, Movie) for movie in movies)
    assert movies == sorted(movies, key=lambda movie: movie.id)


def test_get_by_id(repository):
    movie = repository.get_by_id(1)

    assert movie is not None
    assert isinstance(movie, Movie)
    assert movie.id == 1


def test_id_not_found(repository):
    movie = repository.get_by_id(9999999)

    assert movie is None


def test_get_by_ids(repository):
    movies = repository.get_by_ids([1, 2, 3])

    assert len(movies) > 0
    assert all(isinstance(movie, Movie) for movie in movies)


def test_get_genres_by_id(repository):
    genres = repository.get_genres_by_id(1)

    print(genres)

    assert len(genres) > 0
    assert all(isinstance(genre, Genre) for genre in genres)
