import os
import logging
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine as sqlalchemy_create_engine
from sqlalchemy.engine import Engine, Connection

logger = logging.getLogger(__name__)

def create_engine() -> Engine:

    db_user = os.getenv("POSTGRES_USER")
    db_password = os.getenv("POSTGRES_PASSWORD")
    db_host = os.getenv("POSTGRES_HOST")
    db_port = os.getenv("POSTGRES_PORT")
    db_name = os.getenv("POSTGRES_DB")
    db_driver = os.getenv("POSTGRES_DRIVER", "postgresql+psycopg2")

    if not all([db_user, db_password, db_host, db_port, db_name]):
        logger.error("Variáveis de ambiente do banco não configuradas.")
        raise ValueError(
            "As variáveis de ambiente do banco não estão configuradas corretamente."
        )

    logger.info(
        "Criando conexão com o banco '%s' em %s:%s.", 
        db_name, 
        db_host, 
        db_port
    )

    database_url = (
        f"{db_driver}://"
        f"{db_user}:{db_password}@"
        f"{db_host}:{db_port}/"
        f"{db_name}"
    )

    return sqlalchemy_create_engine(database_url)

def load_dataframe(
    dataframe: pd.DataFrame,
    table_name: str,
    connection: Connection,
    schema: str = "public",
    if_exists: str = "append",
    chunksize: int = 1000,
) -> None:

    if dataframe.empty:
        logger.warning(
            "Tentativa de carregar DataFrame vazio para %s.%s.",
            schema,
            table_name,
        )
        raise ValueError("DataFrame vazio.")

    logger.info(
            "Iniciando carga de %d registros para %s.%s.",
            len(dataframe),
            schema,
            table_name,
        )
    
    try:
        dataframe.to_sql(
            name=table_name,
            con=connection,
            schema=schema,
            if_exists=if_exists,
            index=False,
            chunksize=chunksize,
            method="multi",
        )

        logger.info(
            "Carga concluída com sucesso. %d registros inseridos em %s.%s.",
            len(dataframe),
            schema,
            table_name,
        )

    except Exception as e:
        logger.exception(
            "Erro ao carregar dados para %s.%s.",
            schema,
            table_name,
        )
        raise RuntimeError(
            f"Erro ao carregar dados: {e}"
        ) from e