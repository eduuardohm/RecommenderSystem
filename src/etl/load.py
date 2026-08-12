import os
import logging
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine as sqlalchemy_create_engine
from sqlalchemy.engine import Engine, Connection

logger = logging.getLogger(__name__)

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