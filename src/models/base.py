# ORM: object relational mapping
# Com essa extensão do sqlalchemy, podemos editar banco de dados SQL por meio
# de objetos em python.
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass