from dotenv import load_dotenv
import os
from pymongo import MongoClient


load_dotenv()
SERVER=os.getenv('SERVER')
# Conectar al servidor de MongoDB
client = MongoClient(SERVER)

# Seleccionar la base de datos ecrm
db = client['ecrm']

# Verificar la conexión a la base de datos
try:
    # Verificar la conexión
    server_info = client.server_info()  # Esto confirmará que estamos conectados al servidor
    print("Conexión exitosa al servidor de MongoDB")
    print("Información del servidor:", server_info)

    # Listar las colecciones en la base de datos ecrm
    collections = db.collection_names()  # Método compatible con pymongo 3.4.0
    print("Colecciones en la base de datos ecrm:", collections)

    # Acceder a documentos en una colección específica, por ejemplo 'users'
    collection_name = 'users'
    if collection_name in collections:
        print(f"Accediendo a documentos en la colección {collection_name}:")
        collection = db[collection_name]
        documents = collection.find().limit(5)  # Obtener los primeros 5 documentos
        for doc in documents:
            print(doc)
    else:
        print(f"La colección {collection_name} no existe en la base de datos ecrm.")
except Exception as e:
    print(f"Ocurrió un error: {e}")