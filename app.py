from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    name: str
    description: str
    id: int
    status: bool


data = []


@app.post("/task")
async def post(task: Task):
    data.append(task)
    return task


@app.get("/task")
async def getAll():
    return data

@app.get(f"/task/{id}")
async def get(id):
    return data[id]

@app.put(f"/task/{id}")
async def put(task: Task):
    data.remove(id)
    data.append(task)
    return {"message":"put"}


@app.delete(f"/task/{id}")
async def delete():
    data.remove(id)
    return {"message":"delete"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
