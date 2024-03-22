# ● Создайте модуль приложения и настройте сервер и маршрутизацию.
# ● Создайте класс Movie с полями id, title, description и genre.
# ● Создайте список movies для хранения фильмов.
# ● Создайте маршрут для получения списка фильмов по жанру (метод GET).
# ● Реализуйте валидацию данных запроса и ответа.

import uvicorn
from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str


movies = [
    Movie(id=1, title="Movie Шляпа", description="Description 1", genre="Action"),
    Movie(id=2, title="Movie Перчатки", description="Description 2", genre="Comedy"),
    Movie(id=3, title="Movie Вокзал", description="Description 3", genre="Action"),
    Movie(id=4, title="Movie Вокзал", description="Description 3", genre="Action"),
    Movie(id=5, title="Movie Вокзал", description="Description 3", genre="Action"),
    Movie(id=6, title="Movie Упырь", description="Description 4", genre="Drama"),
]


@app.get("/")
async def root():
    return movies


@app.get("/movies/")
def get_movies_by_genre(
        genre: str = Query(..., title="Genre",
                           description="Genre of the movies to filter",
                           min_length=3)):
    filtered_movies = [movie for movie in movies if movie.genre.lower() == genre.lower()]
    return filtered_movies


if __name__ == "__main__":
    uvicorn.run("task_01:app", host="127.0.0.1", port=8000)
