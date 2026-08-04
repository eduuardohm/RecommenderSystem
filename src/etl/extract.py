import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def extract_csv(file_path: str, filename: str, **kwargs) -> pd.DataFrame:
    """
    Lê um arquivo CSV e retorna um dataframe pandas.

    Raises:
        FileNotFoundError: Arquivo não encontrado.
        RuntimeError: Erro durante a leitura do arquivo.
        ValueError: Arquivo vazio.
    """

    path = Path(file_path).joinpath(filename)

    if not path.exists():
        logger.error("Arquivo não encontrado: %s", path)
        raise FileNotFoundError(
            f"Arquivo não encontrado: {filename}"
        )
    
    logger.info("Lendo arquivo %s", path)

    try: 
        df = pd.read_csv(path, **kwargs)
    except Exception as e:
        logger.exception("Erro ao ler %s", path)
        raise RuntimeError(
            f"Erro ao ler {filename}: {e}"
        )

    if df.empty:
        logger.warning("Arquivo %s está vazio.", path)
        raise ValueError(
            f"O arquivo {filename} está vazio."
        )

    logger.info("Arquivo %s lido com sucesso.", path)

    return df