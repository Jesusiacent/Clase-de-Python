#pip install fastapi uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
#async def raiz():
    #return{'Message': 'Hello World'}
def raiz():
    return{'Hola': 'world'} # para correrlo abrir terminal y colocamos: cd api y damos enter. em la siguinete colocamos 'uvicorn (nombre de archivo):app --reload


@app.get('/libross/{id}')
def read_item(id: int):
    return {'data': id}

@app.post('/libros/')
async def insertar_libro(libro: Libro):
    return {'Massege': f'Libro: {libro.titulo} insertado correctamente'}

    #inst thunder client para revisar paginas raiz propia o creda por nosotros desde el visual 