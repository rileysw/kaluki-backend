from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/add_player/{name}")
def add_player(name: str):
    return name