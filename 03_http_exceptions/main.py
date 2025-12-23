from pydantic import BaseModel, Field, EmailStr
from fastapi import FastAPI, HTTPException

class User(BaseModel):
    username: str = Field(min_length=4, max_length=30)
    email : EmailStr

class Tag(BaseModel):
    name: str
    color: str

class Task(BaseModel):
    title: str = Field(..., min_length=4, max_length=35)
    description: str = Field(default=None, description="опис таски")
    priority: int = Field(..., ge=0,le=10)
    is_finished: bool = Field(default=False)
    author: User
    tags: list[Tag] = []

task_db = []

app = FastAPI()

@app.post("/tasks/", status_code=201)
async def create_tasks(task: Task):
    task_db.append(task)
    return task

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):

    if task_id  len(task_db):
        raise HTTPException(status_code=404, detail="нема такого таску")

    return task_db[task_id]