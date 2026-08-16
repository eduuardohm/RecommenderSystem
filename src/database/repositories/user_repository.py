import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Connection


class UserRepository:

    def __init__(self, connection: Connection):
            self.connection = connection

    def get_all_users(self) -> pd.DataFrame:
            query = text("""
                SELECT id
                FROM users
                ORDER BY id    
            """)
    
            return pd.read_sql(
                query, 
                self.connection
            )

    def get_user_by_id(self, user_id: int) -> pd.DataFrame:
        query = text("""
            SELECT id
            FROM users
            WHERE id = :user_id
        """)
    
        return pd.read_sql(
            query, 
            self.connection,
            params={"user_id": user_id}
        )