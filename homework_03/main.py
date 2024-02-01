from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    headers = {"Content-Type", "application/json"}
    return JSONResponse(content={"item_id": item_id}, headers=headers)


@app.get("/ping", status_code=200)
async def ping():
    headers = {"Content-Type", "application/json"}
    return JSONResponse(content={"message": "pong"}, headers=headers)


@app.get("/")
async def root():
    headers = {"Content-Type", "application/json"}
    return JSONResponse(content={"message": "Hello World"}, headers=headers)
