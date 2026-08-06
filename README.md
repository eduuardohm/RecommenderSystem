<a id="readme-top"></a>

# Sistema de Recomendação utilizando conceitos de clustering

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API_REST-009688)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED)
![Machine Learning](https://img.shields.io/badge/Scikit--Learn-ML-F7931E)

## Descrição

Aplicação *Full-Stack* e de *Machine Learning Engineering* focada na construção de um motor de recomendação de filmes utilizando o famoso dataset **MovieLens**.

Este projeto vai além da simples modelagem matemática, englobando todo o ciclo de vida dos dados: desde o processo de **ETL (Extract, Transform, Load)**, armazenamento relacional estruturado, disponibilização dos modelos via **API REST** e consumo por uma **Interface Web**.

## Contexto e Objetivo

Este projeto foi desenvolvido com o objetivo de aprofundar e consolidar conhecimentos avançados em **Engenharia de Dados, Banco de Dados, Machine Learning e Construção de APIs para IA**. A proposta é simular um ambiente de produção real, onde os dados brutos são processados, armazenados de forma eficiente e consumidos por aplicações clientes.

## Arquitetura do Sistema

O projeto foi desenhado em microsserviços utilizando **Docker** e **Docker Compose**, divididos nas seguintes camadas:

1. **ETL Pipeline:** Scripts responsáveis por ler os dados brutos (`ml-latest-small`), limpar, transformar e persistir no banco de dados.
2. **Database:** Banco de dados **PostgreSQL** para armazenar metadados dos filmes, usuários e histórico de interações (ratings/links).
3. **Machine Learning:** Algoritmos de Filtragem Colaborativa (ex: SVD / Fatoração de Matrizes) treinados para prever a nota que um usuário daria a um filme não assistido.
4. **Backend (API):** Desenvolvido em **FastAPI**, serve como ponte entre o banco de dados, o modelo de ML treinado e o frontend.
5. **Frontend:** Interface de usuário interativa construída para simular uma plataforma de streaming, onde o usuário pode receber recomendações personalizadas.

## Estrutura do Projeto

```
.
├── notebooks/
│   ├── 01_exploracao_movielens.ipynb
│   └── 02_preprocessamento_movielens.ipynb
│
├── data/
│   ├── raw/ml-latest-small/             # Dados brutos do MovieLens (csv)
│   └── processed/                       # Dados transformados pós-ETL (csv limpos)
│
├── src/
│   ├── api/
│   │   ├── main.py                     # Ponto de entrada do FastAPI
│   │   ├── routes/                     # Endpoints da API REST
│   │   └── database.py                 # Conexões e queries com PostgreSQL
│   │
│   ├── etl/
│   │   ├── extract.py                  # Script para carregamento dos dados
│   │   ├── transform.py                # Script para transformação dos dados
│   │   ├── leoad.py                    # Script para carregamento dos dados no banco
│   │   └── pipeline.py                 # Orquestrador do pipeline de ETL
│   │
│   ├── database/
│   │   └── init.sql                    # Inicializa schema do banco
│   │
│   └── services/
│
├── Dockerfile.etl
├── docker-compose.yml
└── README.md
```

### Pré-requisitos
- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados.

## Execução do projeto

1. Clone o repositório e navegue até a pasta raiz do projeto.
2. Configure as variáveis de ambiente (se necessário, renomeie um arquivo `.env.example` para `.env`).
3. Suba os containers com o Docker Compose:

```bash
docker-compose up --build -d
```

Toda a infraestrutura do projeto foi empacotada utilizando o Docker, o que torna a execução extremamente simples, sem a necessidade de instalar dependências locais no seu sistema operacional.

## Funcionalidades

- Pipeline de ETL automatizado em ambiente isolado (`Dockerfile.etl`);
- Banco de dados relacional populado dinamicamente com dados limpos;
- Endpoint RESTful de recomendações de alta performance com FastAPI;
- Sistema de recomendação baseado no histórico de avaliações do usuário (Collaborative Filtering);
- Resolução do problema de *Cold-Start* (recomendação de filmes populares para usuários novos);
- Infraestrutura totalmente dockerizada para fácil deploy.

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




<p align="right">(<a href="#readme-top">back to top</a>)</p>