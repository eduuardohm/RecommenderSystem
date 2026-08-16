import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Connection


class GenreRepository:

    def __init__(self, connection: Connection):
        self.connection = connection

    def get_all_genres(self) -> pd.DataFrame:
        query = text("""
            SELECT id, name
            FROM genres
            ORDER BY id    
        """)

        return pd.read_sql(
            query, 
            self.connection
        )


    def get_genre_by_id(self, genre_id: int) -> pd.DataFrame:
        query = text("""
            SELECT id, name
            FROM genres
            WHERE id = :genre_id
        """)
        return pd.read_sql(
            query, 
            self.connection, 
            params={"genre_id": genre_id}
        )