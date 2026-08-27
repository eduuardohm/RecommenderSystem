from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base
from src.models.genre import Genre

# Guia para relação many-to-many dessa classe: https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#many-to-many

association_table = Table(
    "movie_genres",
    Base.metadata,
    Column("movie_id", ForeignKey("movies.id"), primary_key=True),
    Column("genre_id", ForeignKey("genres.id"), primary_key=True),
)

class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    year: Mapped[int | None]
    genres: Mapped[list[Genre]] = relationship(secondary=association_table)

    def __repr__(self) -> str:
        return f"<Movie(id={self.id}, title={self.title}, year={self.year}, genres={self.genres})>"
