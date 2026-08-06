import os
import logging
from dotenv import load_dotenv

from extract import extract_csv
from transform import (
    transform_movies,
    transform_genres,
    transform_movie_genres,
    transform_users,
    transform_ratings,
)
from load import create_engine, load_dataframe

logger = logging.getLogger(__name__)

def main() -> None:
    load_dotenv()

    logger.info("Iniciando pipeline ETL.")

    try:
        data_path = os.getenv("DATA_PATH")

        if data_path is None:
            raise ValueError(
                "Variável de ambiente DATA_PATH não encontrada."
            )

        engine = create_engine()

        logger.info("Etapa: Extract")

        movies_raw = extract_csv(data_path, "movies.csv")
        ratings_raw = extract_csv(data_path, "ratings.csv")

        logger.info("Etapa: Transform")

        movies = transform_movies(movies_raw)
        genres = transform_genres(movies_raw)
        movie_genres = transform_movie_genres(movies_raw, genres)
        users = transform_users(ratings_raw)
        ratings = transform_ratings(ratings_raw)

        logger.info("Etapa: Load")

        with engine.begin() as connection:

            load_dataframe(users, "users", connection)

            load_dataframe(movies, "movies", connection)

            load_dataframe(genres, "genres", connection)

            load_dataframe(movie_genres, "movie_genres", connection)

            load_dataframe(ratings, "ratings", connection)

        logger.info("Pipeline ETL finalizado com sucesso.")


    except Exception:
        logger.exception(
            "Falha durante a execução do pipeline ETL."
        )
        raise

if __name__ == "__main__":
    main()