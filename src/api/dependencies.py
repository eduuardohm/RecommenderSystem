# get_session() -> yield session
from fastapi import Depends
from sqlalchemy.orm import Session

from src.database.repositories.movie_repository import MovieRepository
from src.database.session import SessionLocal
from src.services.movie_service import MovieService


def get_session():
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()

def get_movie_repository(
        session: Session = Depends(get_session)
    ) -> MovieRepository:
    return MovieRepository(session)

def get_movie_service(
        movie_repository: MovieRepository = Depends(get_movie_repository)
    ) -> MovieService:
    return MovieService(movie_repository)
