from dotenv import load_dotenv
import os
from pymongo import MongoClient
from typing import Optional


load_dotenv()
SERVER=os.getenv('SERVER')
# Conectar al servidor de MongoDB
client = MongoClient(SERVER)

# Seleccionar la base de datos ecrm
db = client['ecrm']

def problemas_cola(db: MongoClient) -> Optional[int]:
    """
    Calcula y muestra la cantidad de problemas en la cola de pagos y recargas de terceros basándose en el tipo de fuente 'TRANSFER'.

    Este método busca en la colección 'payment_extern_operation' todos los documentos donde el campo 'source_type' es igual a 'TRANSFER',
    luego cuenta cuántos de esos documentos existen y finalmente imprime el resultado.

    Args:
        db (MongoClient): El cliente de MongoDB conectado al servidor.

    Returns:
        int | None: La cantidad de problemas encontrados. Retorna None en caso de error.
    """
    try:
        cola = db.get_collection('payment_extern_operation').find({"source_type" : "TRANSFER"}).count()
        print(f"La cantidad de problemas en la cola de pagos y recargas de terceros es: {cola}")
        return cola
    except Exception as e:
        print(f"Error al procesar la consulta: {e}")
        return None


def actualiza_estado_de_cuenta_eCRM(db):
    """
    Actualiza el valor del campo 'insert_sgc_account_state' a 'false' en todos los documentos de la colección 'trace_process'
    donde el campo 'insert_sgc_account_state' contiene el valor 'true', independientemente de su formato (mayúsculas/minúsculas).

    Args:
        db (MongoClient): El cliente de MongoDB conectado al servidor.

    Returns:
        int: El número de documentos actualizados. Retorna 0 si no se encontraron documentos que coincidan con el criterio de búsqueda.
    """
    try:
        actualizacion = db.get_collection('trace_process').update_many(
            {"insert_sgc_account_state": {"$regex": "\"true\"", "$options" : "i"}},  # Criterio de búsqueda
            {"$set": {"insert_sgc_account_state": "false"}}  # Operación de actualización
        )
        conteo = 0
        if actualizacion.modified_count != None:
            conteo = actualizacion.modified_count
        print(f'La cantidad de documentos encontrados y con el campo insert_sgc_account_state puestos en false es: {conteo}')
        

    except Exception as e:
        print(f'Error al procesar la consulta: {e}')
        return None
    return conteo

problemas_cola(db)
actualiza_estado_de_cuenta_eCRM(db)
