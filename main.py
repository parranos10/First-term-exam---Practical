from fastapi import FastAPI
from sqlmodel import SQLModel
from typing import Optional

app = FastAPI()


class User(SQLModel):
    id: Optional[int] = None
    username: str
    password: str
    email: Optional[str] = None
    is_active: bool = True


db_users = [
    User(id=1, username="admin", password="admin"),
    User(id=2, username="user", password="user"),
    User(id=3, username="guest", password="guest")
]

current_id = 4


@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.post("/users")
def create_user(user: User):
    global current_id

    for u in db_users:
        if u.username == user.username:
            return {"mensaje": "Username ya existe"}

    user.id = current_id
    current_id += 1

    db_users.append(user)
    return user


@app.get("/users")
def get_users():
    return db_users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in db_users:
        if user.id == user_id:
            return user
    return {"mensaje": "Usuario no encontrado"}


@app.put("/users/{user_id}")
def update_user(user_id: int, data: dict):
    for user in db_users:
        if user.id == user_id:
            user.username = data.get("username", user.username)
            user.email = data.get("email", user.email)
            user.is_active = data.get("is_active", user.is_active)
            return user
    return {"mensaje": "Usuario no encontrado"}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in db_users:
        if user.id == user_id:
            db_users.remove(user)
            return {"mensaje": "Usuario eliminado"}
    return {"mensaje": "Usuario no encontrado"}


@app.post("/login")
def login(user: User):
    for u in db_users:
        if u.username == user.username and u.password == user.password:
            return {"message": "Login exitoso"}

    return {"message": "Credenciales incorrectas"}
