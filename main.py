from fastapi import FastAPI

from . import schemas

from typing import Optional



app = FastAPI()


@app.get('/blog')
def index(limit):
    return {'data': {'name': {limit}}}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.post('/items')
def create_item(request: schemas.Item):

    return request


