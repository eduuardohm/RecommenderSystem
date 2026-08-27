from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.genre import Genre
from src.models.movie import Movie


class MovieRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Movie]:
        query = select(Movie).order_by(Movie.id)
        return list(self.session.scalars(query))

    def get_by_id(self, movie_id: int) -> Movie | None:
        return self.session.get(Movie, movie_id)

    def get_by_ids(self, movie_ids: list[int]) -> list[Movie] | None:
        query = select(Movie).where(Movie.id.in_(movie_ids))
        return list(self.session.scalars(query))

    def get_genres_by_id(self, movie_id: int) -> list[Genre] | None:
        query = select(Genre).join(Movie.genres).where(Movie.id == movie_id)
        return list(self.session.scalars(query))
