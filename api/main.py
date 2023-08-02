#pip install fastapi uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
#async def raiz():
    #return{'Message': 'Hello World'}
def raiz():
    return{'Hola': 'world'} # para correrlo abrir terminal y colocamos: cd api y damos enter. em la siguinete colocamos 'uvicorn (nombre de archivo):app --reload


@app.get('/items/{item_id}')
def read_item(item_id: int, m: str = None):
    return {'item_id': item_id, 'm': m}

#@app.post('/items/')
#async def insertar_libro(libro: Libro):
    #return {'Massege': f'Libro: {libro.titulo} isertado correctamente'}

    #inst thunder client para revisar paginas raiz propia o creda por nosotros desde el visual 