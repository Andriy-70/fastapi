from fastapi import FastAPI

app = FastAPI(
    title="Learn FastApi"
)


@app.get("/")
async def ping():
    return {"status": "alive"}

@app.get("/hello/{name}")
async def hello(name: str):
    return {"hello": name}




# fastapi dev ...
# uvicorn main:app --reload