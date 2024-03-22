# Создать API для управления списком задач. Приложение должно иметь возможность создавать, обновлять, удалять и получать
# список задач.
# ● Создайте модуль приложения и настройте сервер и маршрутизацию.
# ● Создайте класс Task с полями id, title, description и status.
# ● Создайте список tasks для хранения задач.
# ● Создайте маршрут для получения списка задач (метод GET).
# ● Создайте маршрут для создания новой задачи (метод POST).
# ● Создайте маршрут для обновления задачи (метод PUT).
# ● Создайте маршрут для удаления задачи (метод DELETE).
# ● Реализуйте валидацию данных запроса и ответа.
import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from random import choice

app = FastAPI()


class Task(BaseModel):
    id_t: int
    title: str
    description: Optional[str] = None
    status: str


statuses = ["to do", "in progress", "done"]
tasks = []
for i in range(1, 6):
    id_t = i
    title = "name_" + str(i)
    description = "description_" + str(i)*3
    status = choice(statuses)
    data = {"id_t": id_t, "title": title, "description": description, "status": status}
    task = Task(**data)
    tasks.append(task)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/data/")
async def receive():
    return {"task_list": tasks}


@app.post("/tasks/")
async def create(task: Task):
    tasks.append(task)
    return task


@app.put("/tasks/{task_id}")
async def updating(id_t: int, task: Task):
    for i in range(len(tasks)):
        if tasks[i].id_t == id_t:
            tasks[i] = task
    return {"id_t": id_t, "task": task}


@app.delete("/tasks/{task_id}")
async def delete_data(id_t: int):
    for task in tasks:
        if task.id_t == id_t:
            tasks.remove(task)
    print(tasks)
    return {"id_t": id_t}


if __name__ == "__main__":
    uvicorn.run("task_01:app", host="127.0.0.1", port=8000)
