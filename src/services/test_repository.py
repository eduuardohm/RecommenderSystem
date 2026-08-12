from src.database.connection import create_engine
from src.database.repositories.movie_repository import MovieRepository

engine = create_engine()

with engine.connect() as connection:
    repository = MovieRepository(connection)

    movies = repository.get_all_movies()

    print(movies.head())
    print(f"Tamanho: {len(movies)}")