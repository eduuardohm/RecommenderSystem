import pandas as pd
import logging

logger = logging.getLogger(__name__)

def transform_movies(df: pd.DataFrame) -> pd.DataFrame:
    """
        Transforma o dataset de filmes separando o título do ano.

        Raises:
            ValueError: DataFrame vazio.
            RuntimeError: Erro durante a transformação.
    """
    if df.empty:
        logger.warning("DataFrame de filmes está vazio.")
        raise ValueError("O DataFrame de filmes está vazio.")

    required_columns = {"movieId", "title", "genres"}

    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Colunas ausentes: {missing}"
        )

    logger.info("Iniciando transformação do dataset de filmes.")

    try:
        transformed_df = df.copy()

        transformed_df = transformed_df.rename(
            columns={
                "movieId": "id"
            }
        )

        transformed_df["title"] = transformed_df["title"].str.strip()

        transformed_df["year"] = (
            pd.to_numeric(
                transformed_df["title"].str.extract(r"\((\d{4})\)$")[0],
                errors="coerce",
            )
            .astype("Int64")
        )

        transformed_df["title"] = (
            transformed_df["title"].str.replace(r"\s\(\d{4}\)$", "", regex=True)
        )

        transformed_df = transformed_df.drop(
            columns=["genres"]
        )

    except Exception as e:
        logger.exception("Erro durante a transformação do dataset de filmes.")
        raise RuntimeError(
            f"Erro ao transformar dataset de filmes: {e}"
        ) from e

    logger.info("Transformação do dataset de filmes concluída com sucesso.")

    return transformed_df

def transform_genres(df: pd.DataFrame) -> pd.DataFrame:
    """
        Gera o DataFrame de gêneros a partir do DataFrame de filmes.
        
        Raises:
            ValueError: DataFrame vazio.
            RuntimeError: Erro durante a transformação.
    """

    if df.empty:
        logger.warning("DataFrame de filmes está vazio.")
        raise ValueError("O DataFrame de filmes está vazio.")

    required_columns = {"genres"}

    missing = required_columns - set(df.columns)
    
    if missing:
        raise ValueError(
            f"Colunas ausentes: {missing}"
        )

    logger.info("Iniciando transformação do dataset de filmes para o DataFrame de gêneros.")

    try:
        transformed_df = df.copy()

        transformed_df = transformed_df[["genres"]]

        transformed_df["genres"] = transformed_df["genres"].str.split("|")

        transformed_df = transformed_df.explode("genres")

        transformed_df = (
            transformed_df
            .drop_duplicates()
            .sort_values("genres")
            .reset_index(drop=True)
        )

        transformed_df = transformed_df.rename(
            columns={
                "genres": "name"
            }
        )

        transformed_df["id"] = range(1, len(transformed_df) + 1)

        transformed_df = transformed_df[["id", "name"]]

    except Exception as e:
        logger.exception("Erro durante a transformação do DataFrame de gêneros.")
        raise RuntimeError(
            f"Erro ao transformar DataFrame de filmes: {e}"
        ) from e

    logger.info("Transformação do dataset de gêneros concluída com sucesso.")
    
    return transformed_df

def transform_movie_genres(
    movies_df: pd.DataFrame, 
    genres_df: pd.DataFrame
) -> pd.DataFrame:
    """
        Gera o DataFrame de movie_genres a partir do DataFrame de ratings.
        
        Raises:
            ValueError: DataFrame vazio.
            RuntimeError: Erro durante a transformação.
    """
    if movies_df.empty or genres_df.empty:
        logger.warning("DataFrame de filmes está vazio.")
        raise ValueError("O DataFrame de filmes está vazio.")

    required_movies = {"movieId", "genres"}
    missing = required_movies - set(movies_df.columns)
    if missing:
        raise ValueError(
            f"Colunas ausentes em movies_df: {missing}"
        )

    required_genres = {"id", "name"}
    missing = required_genres - set(genres_df.columns)
    if missing:
        raise ValueError(
            f"Colunas ausentes em genres_df: {missing}"
        )

    try:
        transformed_df = movies_df[
            ["movieId", "genres"]
        ].copy()

        transformed_df["genres"] = (
            transformed_df["genres"].str.split("|")
        )

        transformed_df = transformed_df.explode("genres")

        transformed_df = transformed_df.merge(
            genres_df,
            left_on="genres",
            right_on="name",
            how="left"
        )

        transformed_df = transformed_df.rename(
            columns={
                "movieId": "movie_id",
                "id": "genre_id"
            }
        )

        transformed_df = transformed_df[
            ["movie_id", "genre_id"]
        ]


    except Exception as e:
        logger.exception("Erro durante a transformação do DataFrame de gêneros de filmes.")
        raise RuntimeError(
            f"Erro ao transformar DataFrame de gêneros de filmes: {e}"
        ) from e

    if transformed_df["genre_id"].isna().any():
        raise ValueError(
            "Existem gêneros sem correspondência."
        )
    
    logger.info("Transformação do dataset de gêneros de filmes concluída com sucesso.")

    return transformed_df
        
def transform_users(df: pd.DataFrame) -> pd.DataFrame:
    """
        Gera o DataFrame de users a partir do DataFrame de ratings.
        
        Raises:
            ValueError: DataFrame vazio.
            RuntimeError: Erro durante a transformação.
    """
    if df.empty:
        logger.warning("DataFrame de ratings está vazio.")
        raise ValueError("O DataFrame de ratings está vazio.")

    required_columns = {"userId"}

    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Colunas ausentes: {missing}"
        )

    logger.info("Iniciando transformação do dataset de users.")

    try:
        transformed_df = df.copy()

        transformed_df = transformed_df[["userId"]]

        transformed_df = (
            transformed_df
            .drop_duplicates()
            .sort_values("userId")
            .reset_index(drop=True)
        )

        transformed_df = transformed_df.rename(
            columns={
                "userId": "id"
            }
        )

    except Exception as e:
        logger.exception("Erro durante a transformação do DataFrame de usuários.")
        raise RuntimeError(
            f"Erro ao transformar DataFrame de usuários: {e}"
        ) from e

    logger.info("Transformação do dataset de usuários concluída com sucesso.")

    return transformed_df

def transform_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """
        Gera o DataFrame de ratings a partir do DataFrame de ratings.
        
        Raises:
            ValueError: DataFrame vazio.
            RuntimeError: Erro durante a transformação.
    """

    if df.empty:
        logger.warning("DataFrame de ratings está vazio.")
        raise ValueError(
            "O DataFrame de ratings está vazio."
        )

    required_columns = {"userId", "movieId", "rating", "timestamp"}

    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Colunas ausentes: {missing}"
        )

    logger.info("Iniciando transformação do dataset de ratings.")

    try:
        transformed_df = df.copy()

        transformed_df = transformed_df.rename(
            columns={
                "userId": "user_id",
                "movieId": "movie_id",
                "timestamp": "rated_at"
            }
        )

        transformed_df["rated_at"] = pd.to_datetime(
            transformed_df["rated_at"],
            unit="s"
        )

    except Exception as e:
        logger.exception("Erro durante a transformação do DataFrame de ratings.")
        raise RuntimeError(
            f"Erro ao transformar DataFrame de avaliações: {e}"
        ) from e

    logger.info("Transformação do dataset de avaliações concluída com sucesso.")

    return transformed_df