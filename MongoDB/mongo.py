import pymongo

# Establecer la conexión a MongoDB (asegúrate de cambiar la URL y el puerto según tu configuración)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Seleccionar una base de datos (si no existe, se creará automáticamente)
db = client["books"]

# Insertar un documento en una colección llamada 'mi_coleccion'
mi_coleccion = db["books"]

# Leer todos los documentos en la colección
documentos = mi_coleccion.find({})
for doc in documentos:
    print(doc)

from pymongo import MongoClient
import bson

# Leer la imagen como binario
with open('./Marvy.png', 'rb') as file:
    image_data = file.read()

# Crear un documento con el binario de la imagen
document = {
    'nombre': 'Marvy',
    'imagen': bson.Binary(image_data),
}

# Insertar el documento en la colección
mi_coleccion.insert_one(document)
