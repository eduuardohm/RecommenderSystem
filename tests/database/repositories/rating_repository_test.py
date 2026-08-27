import pytest

from src.database.repositories.rating_repository import RatingRepository
from src.database.session import SessionLocal
from src.models.rating import Rating


@pytest.fixture
def repository():
    with SessionLocal() as session:
        yield RatingRepository(session)


def test_get_all(repository):
    ratings = repository.get_all()

    assert len(ratings) > 0
    assert all(isinstance(rating, Rating) for rating in ratings)


def test_get_by_movie_returns_ratings(repository):
    ratings = repository.get_by_movie(1)

    assert len(ratings) > 0


def test_get_by_movie_without_ratings(repository):
    ratings = repository.get_by_movie(999999)

    assert ratings == []