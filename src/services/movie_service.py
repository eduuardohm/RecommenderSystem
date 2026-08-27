from src.database.repositories.movie_repository import MovieRepository
from src.models.movie import Movie


class MovieService:

    def __init__(self, movie_repository: MovieRepository):
        self.movie_repository = movie_repository

    def get_all(self) -> list[Movie]:
        return self.movie_repository.get_all()

    def get_by_id(self, id: int) -> Movie:
        return self.movie_repository.get_by_id(movie_id=id)