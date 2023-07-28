#pip install fastapi uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz():
    return{'Hola': 'world'} # para correrlo abrir terminal y colocamos: cd api y damos enter. em la siguinete colocamos 'uvicorn (nombre de archivo):app --reload


@app.get('/items/{item_id}')
def read_item(item_id: int, m: str = None):
    return {'item_id': item_id, 'm': m}