from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class Rating(Base):
    __tablename__ = "ratings"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), 
        primary_key=True,
    )
    movie_id: Mapped[int] = mapped_column(
        ForeignKey("movies.id"),
        primary_key=True,
    )
    rating: Mapped[float] = mapped_column(nullable=False)
    rated_at: Mapped[datetime] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (
            f"<Rating("
            f"user_id={self.user_id}, "
            f"movie_id={self.movie_id}, "
            f"rating={self.rating}, "
            f"rated_at={self.rated_at}"
            f")>"
        )
