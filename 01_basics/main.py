from fastapi import FastAPI, Depends

app = FastAPI(
    title="Learn FastApi"
)


@app.get("/")
async def ping():
    return {"status": "alive"}

@app.get("/hello/{name}")
async def hello(name: str):
    return {"hello": name}

def get_query(q: str | None = None):
    return q

@app.get("/items")
async def read_items(query: str = Depends(get_query)):
    return {"result": query}

# fastapi dev ...
# uvicorn main:app --reload