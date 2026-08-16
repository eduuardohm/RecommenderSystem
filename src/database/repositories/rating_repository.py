import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Connection


class RatingRepository:

    def __init__(self, connection: Connection):
        self.connection = connection

    def get_all_ratings(self) -> pd.DataFrame:
        query = text("""
            SELECT *
            FROM ratings
            ORDER BY movie_id    
        """)

        return pd.read_sql(
            query, 
            self.connection
        )

    def get_ratings_by_user(self, user_id: int) -> pd.DataFrame:
        query = text("""
            SELECT *
            FROM ratings
            WHERE user_id = :user_id
        """)

        return pd.read_sql(
            query,
            self.connection,
            params={"user_id": user_id}
        )

    def get_ratings_by_movie(self, movie_id: int) -> pd.DataFrame:
            query = text("""
                SELECT *
                FROM ratings
                WHERE movie_id = :movie_id
            """)
    
            return pd.read_sql(
                query,
                self.connection,
                params={"movie_id": movie_id}
            )