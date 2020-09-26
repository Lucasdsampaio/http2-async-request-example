from fastapi import FastAPI
from time import sleep

app = FastAPI()


@app.get("/teste1")
def teste_1():
    sleep(4)
    return {"Hello": "World"}

@app.get("/teste2")
def teste_2():
    sleep(4)
    return {"Hello": "World2"}