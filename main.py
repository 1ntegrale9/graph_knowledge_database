from fastapi import FastAPI
from gkb import get_keys, get_values

app = FastAPI()


@app.get('/')
def read_tags_all():
    return {'tags': get_keys()}

@app.get('/{tag}')
def read_tags(tag: str):
    return {'tags': get_values(tag)}
