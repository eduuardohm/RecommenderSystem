import os

from dotenv import load_dotenv
from sqlalchemy import create_engine as sqlalchemy_create_engine
from sqlalchemy.engine import URL, Engine

load_dotenv()

def create_engine() -> Engine:
    db_user = os.getenv("POSTGRES_USER")
    db_password = os.getenv("POSTGRES_PASSWORD")
    db_host = os.getenv("POSTGRES_HOST")
    db_port = os.getenv("POSTGRES_PORT")
    db_name = os.getenv("POSTGRES_DB")
    db_driver = os.getenv("POSTGRES_DRIVER", "postgresql+psycopg2")

    if not all([db_user, db_password, db_host, db_port, db_name]):
        raise ValueError(
            "As variáveis de ambiente do banco não estão configuradas corretamente."
        )

    database_url = URL.create(
        drivername=db_driver,
        username=db_user,   
        password=db_password,
        host=db_host,
        port=int(db_port),
        database=db_name
    )

    return sqlalchemy_create_engine(database_url)