import pytest

from src.database.repositories.genre_repository import GenreRepository
from src.database.session import SessionLocal
from src.models.genre import Genre


@pytest.fixture
def repository():
    with SessionLocal() as session:
        yield GenreRepository(session)


def test_get_all(repository):
    genres = repository.get_all()

    assert len(genres) > 0
    assert all(isinstance(genre, Genre) for genre in genres)
    assert genres == sorted(genres, key=lambda genre: genre.id)

