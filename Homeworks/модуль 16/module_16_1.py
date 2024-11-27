from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome() -> dict:
    return {'message': 'Главная страница'}


@app.get('/user/admin')
async def hello_admin() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get("/user/{user_id}")
async def hello_user(_id: int) -> dict:
    return {'message:': f'Вы вошли как пользователь №{_id}'}


@app.get('/user')
async def info(username: str, age: int):
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}
