import pandas as pd

from sqlalchemy import text
from sqlalchemy.engine import Connection

class MovieRepository:

    def __init__(self, connection: Connection):
        self.connection = connection

    def get_all_movies(self) -> pd.DataFrame:
        query = text("""
            SELECT
                    id,
                    title,
                    year
            FROM movies
            ORDER BY id    
        """)

        return pd.read_sql(query, self.connection)