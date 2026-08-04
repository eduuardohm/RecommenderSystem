import os
from pathlib import Path
from extract import extract_csv
from dotenv import load_dotenv

load_dotenv()

data_path = os.getenv("DATA_PATH")
if data_path is None:
    raise ValueError(
        "Variável de ambiente 'DATA_PATH' não definida."
    )

DATA_PATH = Path(data_path)

def main():
    movies = extract_csv(DATA_PATH, "movies.csv")
    print(movies.head())

if __name__ == "__main__":
    main()