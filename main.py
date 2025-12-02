from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Workout(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/workout/{workout_id}")
def read_item(workout_id: int, q: Union[str, None] = None):
    return {"workout_id": workout_id, "q": q}

@app.put("/workout/{workout_id}")
def update_item(workout_id: int, workout:Workout):
    return {"workout_id": workout_id, "workout": workout}

@app.post("/workout/")
def create_item(workout: Workout):
    return workout

@app.delete("/workout/{workout_id}")
def delete_item(workout_id: int):
    return {"workout_id": workout_id, "status": "deleted"}

@app.post("/login/")
def login(username: str, password: str):
    return {"username": username}

@app.post("/register/")
def register(username: str, email: str, password: str):
    return {"username": username, "email": email}
