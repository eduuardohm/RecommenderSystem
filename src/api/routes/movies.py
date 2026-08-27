from fastapi import APIRouter, Depends

from src.api.dependencies import get_movie_service
from src.services.movie_service import MovieService

movie_router = APIRouter(prefix="/movies", tags=["movies"])

@movie_router.get("/")
async def movies(movie_service: MovieService = Depends(get_movie_service)):
    return movie_service.get_all()

@movie_router.get("/{movie_id}")
async def movie_by_id(
    movie_id: int,
    movie_service: MovieService = Depends(get_movie_service),
):
    return movie_service.get_by_id(movie_id)