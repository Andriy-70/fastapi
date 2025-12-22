from pydantic import BaseModel, Field, EmailStr
from fastapi import FastAPI

class User(BaseModel):
    username: str = Field(min_length=4, max_length=30)
    email : EmailStr

class Task(BaseModel):
    title: str = Field(..., min_length=4, max_length=35)
    description: str = Field(default=None, description="опис таски")
    priority: int = Field(..., ge=0,le=10)
    is_finished: bool = Field(default=False)
    author: User

    def __str__(self):
        return (f"title: {self.title}\n"
                f"desc: {self.description}\n"
                f"priority: {self.priority}\n"
                f"is_finished: {self.is_finished}")


app = FastAPI(
    title="Learn FastaApi"
)

@app.post("/task/create")
async def create_task(task: Task):
    print(task)
    return {"message": "Task created", "data": task}