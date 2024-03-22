# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Реализуйте валидацию данных запроса и ответа.

import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel, EmailStr, constr
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates("templates")


class User(BaseModel):
    u_id: int
    name: str
    email: EmailStr
    password: constr(
        min_length=2,
        max_length=8
    )


users = [
    User(u_id=1, name="Ivan", email="ivan@mail.ru", password="123"),
    User(u_id=2, name="Petr", email="petr@mail.ru", password="456"),
    User(u_id=3, name="Semen", email="semen@mail.ru", password="789"),
    User(u_id=4, name="Igor", email="igor@mail.ru", password="987")
]


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("main_task.html", {"request": request, "users": users})


@app.post("/append/", response_class=HTMLResponse)
async def create(request: Request, user: User):
    users.append(user)
    return templates.TemplateResponse("main_task.html", {"request": request, "users": users})


@app.put("/update/{u_id}", response_class=HTMLResponse)
async def updating(u_id: int, user: User, request: Request):
    for i in range(len(users)):
        if users[i].u_id == u_id:
            users[i] = user
    return templates.TemplateResponse("main_task.html", {"request": request, "users": users})


@app.delete("/delete/{u_id}", response_class=HTMLResponse)
async def delete_data(u_id: int, request: Request):
    for user in users:
        if user.u_id == u_id:
            users.remove(user)
    return templates.TemplateResponse("main_task.html", {"request": request, "users": users})


if __name__ == "__main__":
    uvicorn.run("main_task:app", host="127.0.0.1", port=8000)
