from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()


@app.get('/')
async def welcome() -> dict:
    return {'message': 'Главная страница'}


@app.get('/user/admin')
async def hello_admin() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get("/user/{user_id}")
async def hello_user(_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]) -> dict:
    return {'message:': f'Вы вошли как пользователь №{_id}'}


@app.get('/user/{username}/{age}')
async def info(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                                             example="Einstein")],
               age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="76")]):
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}