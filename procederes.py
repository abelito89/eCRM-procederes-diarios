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


def cierra_gestiones_de_cobro_eCRM(db):
    """
    Actualiza el valor del campo 'get_service_to_call_data_from_sgc' a 'false' en todos los documentos de la colección 'trace_process'
    donde el campo 'get_service_to_call_data_from_sgc' contiene el valor 'true', independientemente de su formato (mayúsculas/minúsculas).

    Args:
        db (MongoClient): El cliente de MongoDB conectado al servidor.

    Returns:
        int: El número de documentos actualizados. Retorna 0 si no se encontraron documentos que coincidan con el criterio de búsqueda.
    """
    try:
        actualizacion = db.get_collection('trace_process').update_many(
            {"get_service_to_call_data_from_sgc": {"$regex": "\"true\"", "$options" : "i"}},  # Criterio de búsqueda
            {"$set": {"get_service_to_call_data_from_sgc": "false"}}  # Operación de actualización
        )
        conteo = 0
        if actualizacion.modified_count != None:
            conteo = actualizacion.modified_count
        print(f'La cantidad de documentos encontrados y con el campo get_service_to_call_data_from_sgc puestos en false es: {conteo}')
        

    except Exception as e:
        print(f'Error al procesar la consulta: {e}')
        return None
    return conteo


def export_fichero_Transfermovil_eCRM(db):
    """
    Actualiza el valor del campo 'export_tranfermovil_operation' a 'false' en todos los documentos de la colección 'trace_process'
    donde el campo 'export_tranfermovil_operation' contiene el valor 'true', independientemente de su formato (mayúsculas/minúsculas).

    Args:
        db (MongoClient): El cliente de MongoDB conectado al servidor.

    Returns:
        int: El número de documentos actualizados. Retorna 0 si no se encontraron documentos que coincidan con el criterio de búsqueda.
    """
    try:
        actualizacion = db.get_collection('trace_process').update_many(
            {"export_tranfermovil_operation": {"$regex": "\"true\"", "$options" : "i"}},  # Criterio de búsqueda
            {"$set": {"export_tranfermovil_operation": "false"}}  # Operación de actualización
        )
        conteo = 0
        if actualizacion.modified_count != None:
            conteo = actualizacion.modified_count
        print(f'La cantidad de documentos encontrados y con el campo export_tranfermovil_operation puestos en false es: {conteo}')
        

    except Exception as e:
        print(f'Error al procesar la consulta: {e}')
        return None
    return conteo


def descarga_fichero_banco_eCRM(db):
    """
    Actualiza el valor del campo 'insert_in_mongo_ftp_files' a 'false' en todos los documentos de la colección 'trace_process'
    donde el campo 'insert_in_mongo_ftp_files' contiene el valor 'true', independientemente de su formato (mayúsculas/minúsculas).

    Args:
        db (MongoClient): El cliente de MongoDB conectado al servidor.

    Returns:
        int: El número de documentos actualizados. Retorna 0 si no se encontraron documentos que coincidan con el criterio de búsqueda.
    """
    try:
        actualizacion = db.get_collection('trace_process').update_many(
            {"insert_in_mongo_ftp_files": {"$regex": "\"true\"", "$options" : "i"}},  # Criterio de búsqueda
            {"$set": {"insert_in_mongo_ftp_files": "false"}}  # Operación de actualización
        )
        conteo = 0
        if actualizacion.modified_count != None:
            conteo = actualizacion.modified_count
        print(f'La cantidad de documentos encontrados y con el campo insert_in_mongo_ftp_files puestos en false es: {conteo}')
        

    except Exception as e:
        print(f'Error al procesar la consulta: {e}')
        return None
    return conteo


def crea_tablas_old_debt_comercial_eCRM(db):
    """
    Actualiza el valor del campo 'created_old_debt' a 'false' en todos los documentos de la colección 'trace_process'
    donde el campo 'created_old_debt' contiene el valor 'true', independientemente de su formato (mayúsculas/minúsculas).

    Args:
        db (MongoClient): El cliente de MongoDB conectado al servidor.

    Returns:
        int: El número de documentos actualizados. Retorna 0 si no se encontraron documentos que coincidan con el criterio de búsqueda.
    """
    try:
        actualizacion = db.get_collection('trace_process').update_many(
            {"created_old_debt": {"$regex": "\"true\"", "$options" : "i"}},  # Criterio de búsqueda
            {"$set": {"created_old_debt": "false"}}  # Operación de actualización
        )
        conteo = 0
        if actualizacion.modified_count != None:
            conteo = actualizacion.modified_count
        print(f'La cantidad de documentos encontrados y con el campo created_old_debt puestos en false es: {conteo}')
        

    except Exception as e:
        print(f'Error al procesar la consulta: {e}')
        return None
    return conteo


def concilia_cobros_transfermovil_eCRM(db):
    """
    Actualiza el valor del campo 'daily_conciliation_transfer_payments' a 'false' en todos los documentos de la colección 'trace_process'
    donde el campo 'daily_conciliation_transfer_payments' contiene el valor 'true', independientemente de su formato (mayúsculas/minúsculas).

    Args:
        db (MongoClient): El cliente de MongoDB conectado al servidor.

    Returns:
        int: El número de documentos actualizados. Retorna 0 si no se encontraron documentos que coincidan con el criterio de búsqueda.
    """
    try:
        actualizacion = db.get_collection('trace_process').update_many(
            {"daily_conciliation_transfer_payments": {"$regex": "\"true\"", "$options" : "i"}},  # Criterio de búsqueda
            {"$set": {"daily_conciliation_transfer_payments": "false"}}  # Operación de actualización
        )
        conteo = 0
        if actualizacion.modified_count != None:
            conteo = actualizacion.modified_count
        print(f'La cantidad de documentos encontrados y con el campo daily_conciliation_transfer_payments puestos en false es: {conteo}')
        

    except Exception as e:
        print(f'Error al procesar la consulta: {e}')
        return None
    return conteo


def concilia_cobros_semanales_transfermovil_eCRM(db):
    """
    Actualiza el valor del campo 'weekly_conciliation_transfer_payments' a 'false' en todos los documentos de la colección 'trace_process'
    donde el campo 'weekly_conciliation_transfer_payments' contiene el valor 'true', independientemente de su formato (mayúsculas/minúsculas).

    Args:
        db (MongoClient): El cliente de MongoDB conectado al servidor.

    Returns:
        int: El número de documentos actualizados. Retorna 0 si no se encontraron documentos que coincidan con el criterio de búsqueda.
    """
    try:
        actualizacion = db.get_collection('trace_process').update_many(
            {"weekly_conciliation_transfer_payments": {"$regex": "\"true\"", "$options" : "i"}},  # Criterio de búsqueda
            {"$set": {"weekly_conciliation_transfer_payments": "false"}}  # Operación de actualización
        )
        conteo = 0
        if actualizacion.modified_count != None:
            conteo = actualizacion.modified_count
        print(f'La cantidad de documentos encontrados y con el campo weekly_conciliation_transfer_payments puestos en false es: {conteo}')
        

    except Exception as e:
        print(f'Error al procesar la consulta: {e}')
        return None
    return conteo

while True:
    print("Elija el proceder que desea ejecutar, teclee el número del consecutivo y presione Enter a continuación")
    print("")
    print("1 - Visualizar la cantidad de problemas con la cola de pagos y recargas de terceros")
    print("2 - Consultar y corregir los documentos que fallaron al actualizarse el estado de cuenta del eCRM")
    print("3 - Consultar y corregir los documentos que fallaron al cerrar las gestiones de cobro que han sido pagadas")
    print("4 - Consultar y corregir los documentos que fallaron al descargar el fichero que contiene todas las operaciones de eCRM recibidas por transfermóvil")
    print("5 - Consultar y corregir los documentos que fallaron al descargar del ftp espejo los ficheros de los bancos para poder ser visualizados y procesados por Facturación")
    print("6 - Consultar y corregir los documentos que fallaron al actualizar o crear las tablas para la edad de la deuda (Comercial)")
    print("7 - Consultar y corregir los documentos que fallaron al conciliar los cobros diarios reportados por el banco como aplicados usando Transfermovil")
    print("8 - Consultar y corregir los documentos que fallaron al conciliar los cobros semanales reportados por el banco como aplicados usando Transfermovil")
    print("9 - Aplicar todos los procederes de manera consecutiva")
    print("Para finalizar la aplicación presione la letra (s)")
    accion = str(input())
    if accion == "1":
        problemas_cola(db)
        pausa = str(input())
    elif accion == "2":
        actualiza_estado_de_cuenta_eCRM(db)
        pausa = str(input())
    elif accion == "3":
        cierra_gestiones_de_cobro_eCRM(db)
        pausa = str(input())
    elif accion == "4":
        export_fichero_Transfermovil_eCRM(db)
        pausa = str(input())
    elif accion == "5":
        descarga_fichero_banco_eCRM(db)
        pausa = str(input())
    elif accion == "6":
        crea_tablas_old_debt_comercial_eCRM(db)
        pausa = str(input())
    elif accion == "7":
        concilia_cobros_transfermovil_eCRM(db)
        pausa = str(input())
    elif accion == "8":
        concilia_cobros_semanales_transfermovil_eCRM(db)
        pausa = str(input())
    elif accion == "9":
        problemas_cola(db)
        actualiza_estado_de_cuenta_eCRM(db)
        cierra_gestiones_de_cobro_eCRM(db)
        export_fichero_Transfermovil_eCRM(db)
        descarga_fichero_banco_eCRM(db)
        crea_tablas_old_debt_comercial_eCRM(db)
        concilia_cobros_transfermovil_eCRM(db)
        concilia_cobros_semanales_transfermovil_eCRM(db)
        pausa = str(input())
    elif accion == "s":
        break


