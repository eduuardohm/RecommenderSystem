from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.genre import Genre


class GenreRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Genre]:
        query = select(Genre).order_by(Genre.id)
        return list(self.session.scalars(query))

    def get_by_id(self, genre_id: int) -> Genre:
        return self.session.get(Genre, genre_id)
