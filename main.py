from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field
from typing import Optional
app = FastAPI()

class User(SQLModel):
    username: str
    password: str

db_users = [
    User(username="admin", password="admin"),
    User(username="user", password="user"),
    User(username="guest", password="guest")
]

@app.get("/")
def read_root():
    return{"Hello":"world"}

@app.post("/login")
def login(user: User):
    if user.username == "admin" and user.password == "1234":
        return {"message": "Login exitoso"}
    else:
        return {"message": "Credenciales incorrectas"}