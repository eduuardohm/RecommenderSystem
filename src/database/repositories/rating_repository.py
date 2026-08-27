from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.rating import Rating


class RatingRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Rating]:
        query = select(Rating).order_by(Rating.movie_id)
        return list(self.session.scalars(query))

    def get_by_movie(self, movie_id: int) -> list[Rating]:
        query = select(Rating).where(Rating.movie_id == movie_id)
        return list(self.session.scalars(query))

    def get_by_user(self, user_id: int) -> list[Rating]:
        query = select(Rating).where(Rating.user_id == user_id)
        return list(self.session.scalars(query))
