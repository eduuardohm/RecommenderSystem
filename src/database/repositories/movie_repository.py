import pandas as pd
from sqlalchemy import bindparam, text
from sqlalchemy.engine import Connection


class MovieRepository:

    def __init__(self, connection: Connection):
        self.connection = connection

    def get_all_movies(self) -> pd.DataFrame:
        query = text("""
            SELECT id, title, year
            FROM movies
            ORDER BY id    
        """)

        return pd.read_sql(
            query, 
            self.connection
        )


    def get_movie_by_id(self, movie_id: int) -> pd.DataFrame:
        query = text("""
            SELECT id, title, year
            FROM movies
            WHERE id = :movie_id
        """)
        return pd.read_sql(
            query, 
            self.connection, 
            params={"movie_id": movie_id}
        )


    def get_movies_by_ids(self, movie_ids: list[int]) -> pd.DataFrame:
        query = text("""
            SELECT id, title, year
            FROM movies
            WHERE id in :movie_ids
            ORDER BY id
        """).bindparams(
            bindparam("movie_ids", expanding=True)
        )

        return pd.read_sql(
            query, 
            self.connection, 
            params={"movie_ids": movie_ids}
        )

    def get_movie_genres(self, movie_id: int) -> pd.DataFrame:
        query = text("""
            SELECT g.id, g.name
            FROM genres g
            INNER JOIN movie_genres mg 
                ON mg.genre_id = g.id
            WHERE mg.movie_id = :movie_id
            ORDER BY g.id;
        """)

        return pd.read_sql(
            query, 
            self.connection, 
            params={"movie_id": movie_id}
        )