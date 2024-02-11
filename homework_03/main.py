from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/ping", status_code=200)
def ping():
    return {"message": "pong"}


@app.get("/")
def root():
    return {"message": "Hello World"}
