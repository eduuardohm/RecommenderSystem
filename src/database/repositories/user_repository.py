from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.user import User


class UserRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        query = select(User).order_by(User.id)
        return list(self.session.scalars(query))

    def get_by_id(self, user_id: int) -> User:
        return self.session.get(User, user_id)
    