from sqlalchemy.orm import sessionmaker

from src.database.connection import create_engine

engine = create_engine()

SessionLocal = sessionmaker(bind=engine)
