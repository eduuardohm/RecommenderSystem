<a id="readme-top"></a>

# Sistema de Recomendação utilizando conceitos de clustering

## Descrição

Este projeto implementa um sistema de recomendação baseado em clustering, utilizando o dataset MovieLens. O objetivo é agrupar filmes e usuários por padrões similares para gerar recomendações personalizadas.

## Estrutura do Projeto

```
.
├── notebooks/
│   ├── 01_exploracao_movielens.ipynb
│   └── 02_preprocessamento_movielens.ipynb
├── src/
│   ├── data/
│   │   └── load.py
│   ├── models/
│   │   └── KMeans.py
│   └── utils/
├── data/
│   ├── raw/
│   │   └── ml-latest-small/
│   │       ├── movies.csv
│   │       ├── ratings.csv
│   │       ├── tags.csv
│   │       ├── links.csv
│   │       └── README.txt
│   └── processed/
│       └── movielens_100k_interactions.csv
└── README.md
```

## Dataset

Utiliza o dataset MovieLens 100K contendo:
- Informações de filmes
- Avaliações de usuários
- Tags de conteúdo
- Interações usuário-filme

## Tecnologias

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

![mlflow](https://img.shields.io/badge/mlflow-%23d9ead3.svg?style=for-the-badge&logo=numpy&logoColor=blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)


## Como Usar

1. Explore os dados com `01_exploracao_movielens.ipynb`
2. Processe os dados com `02_preprocessamento_movielens.ipynb`
3. Treine modelos utilizando os módulos em `src/models/`

## Contato

Eduardo Marques - [@EduardoCodeAI](https://x.com/EduardoCodeAI) - ehms@ic.ufal.br

Link do Projeto - [https://github.com/eduuardohm/RecommenderSystem](https://github.com/eduuardohm/RecommenderSystem) 

<p align="right">(<a href="#readme-top">back to top</a>)</p>