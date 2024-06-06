from fastapi import FastAPI
from model import pub
from uuid import uuid4

app = FastAPI()

publicaciones = []

@app.get('/')
def home():
    return "Hellow from FastApi"

# Aqui leemos todas las públicaciones
@app.get('/pub')
def get_all_pub():
    return publicaciones

# Aqui creamos el insert a la lista
@app.post('/pub')
def insert_pub(pub: pub):
    pub.id = str(uuid4())

    publicaciones.append(pub)
    return f'Row created'

# aqui vamos a leer solo una publicacion
@app.get("/pub/{id_pub}")
def get_one_pub(id_pub: str):

    for pub in publicaciones:

        if pub.id == id_pub:
            return pub
    return 'not found the row'
        
@app.delete("/pub/{id_pub}")
def delete_one_pub(id_pub: str):

    for index, pub in enumerate(publicaciones):
        if pub.id == id_pub:
            print('registro eliminado')
            publicaciones.pop(index)
            return 'Row elimitaded'
    return 'not found the row'
        
@app.put('/pub/{id_pub}')
def update_pub(id_pub: str, pub:pub):
    for index, publ in enumerate(publicaciones):
        if publ.id == id_pub:
            publicaciones[index].titulo = pub.titulo
            publicaciones[index].descripcion = pub.descripcion
            return f'Row updated: {id_pub}'
    
    return 'Not row update'