from fastapi import FastAPI
from src.api.routes.movies import movie_router

app = FastAPI()

app.include_router(movie_router)
