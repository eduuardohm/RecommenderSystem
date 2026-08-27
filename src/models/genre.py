from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class Genre(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement= True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    def __repr__(self) -> str:
        return f"<Genre(id={self.id}, name={self.name})>"
    