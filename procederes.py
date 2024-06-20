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
            {"insert_sgc_account_state": True},  # Criterio de búsqueda
            {"$set": {"insert_sgc_account_state": False}}  # Operación de actualización
        )
        print(f"Resultado de la actualizacion: {actualizacion.raw_result}")
        conteo = actualizacion.modified_count if actualizacion.modified_count is not None else 0
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
            {"get_service_to_call_data_from_sgc": True},  # Criterio de búsqueda
            {"$set": {"get_service_to_call_data_from_sgc": False}}  # Operación de actualización
        )
        print(f"Resultado de la actualizacion: {actualizacion.raw_result}")
        conteo = actualizacion.modified_count if actualizacion.modified_count is not None else 0
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
            {"export_tranfermovil_operation": True},  # Criterio de búsqueda
            {"$set": {"export_tranfermovil_operation": False}}  # Operación de actualización
        )
        print(f"Resultado de la actualizacion: {actualizacion.raw_result}")
        conteo = actualizacion.modified_count if actualizacion.modified_count is not None else 0
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
            {"insert_in_mongo_ftp_files": True},  # Criterio de búsqueda
            {"$set": {"insert_in_mongo_ftp_files": False}}  # Operación de actualización
        )
        print(f"Resultado de la actualizacion: {actualizacion.raw_result}")
        conteo = actualizacion.modified_count if actualizacion.modified_count is not None else 0
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
            {"created_old_debt": True},  # Criterio de búsqueda
            {"$set": {"created_old_debt": False}}  # Operación de actualización
        )
        print(f"Resultado de la actualizacion: {actualizacion.raw_result}")
        conteo = actualizacion.modified_count if actualizacion.modified_count is not None else 0
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
            {"daily_conciliation_transfer_payments": True},  # Criterio de búsqueda
            {"$set": {"daily_conciliation_transfer_payments": False}}  # Operación de actualización
        )
        print(f"Resultado de la actualizacion: {actualizacion.raw_result}")
        conteo = actualizacion.modified_count if actualizacion.modified_count is not None else 0
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
            {"weekly_conciliation_transfer_payments": True},  # Criterio de búsqueda
            {"$set": {"weekly_conciliation_transfer_payments": False}}  # Operación de actualización
        )
        print(f"Resultado de la actualizacion: {actualizacion.raw_result}")
        conteo = actualizacion.modified_count if actualizacion.modified_count is not None else 0
        print(f'La cantidad de documentos encontrados y con el campo weekly_conciliation_transfer_payments puestos en false es: {conteo}')
        

    except Exception as e:
        print(f'Error al procesar la consulta: {e}')
        return None
    return conteo

def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1 - Problemas en cola de pagos y recargas de terceros")
        print("2 - Actualización de estado de cuenta eCRM")
        print("3 - Cierre de gestiones de cobro eCRM")
        print("4 - Exportación de fichero Transfermovil eCRM")
        print("5 - Descarga de fichero banco eCRM")
        print("6 - Creación de tablas de edad de deuda comercial eCRM")
        print("7 - Conciliación de cobros diarios Transfermovil eCRM")
        print("8 - Conciliación de cobros semanales Transfermovil eCRM")
        print("9 - Ejecutar todos los procedimientos")
        print("s - Salir")
        print("\nSeleccione una opción y presione Enter:")

        opcion = input().strip()

        if opcion == "1":
            os.system('cls')
            problemas_cola(db)
            input("Presione Enter para continuar...")
        elif opcion == "2":
            os.system('cls')
            actualiza_estado_de_cuenta_eCRM(db)
            input("Presione Enter para continuar...")
        elif opcion == "3":
            os.system('cls')
            cierra_gestiones_de_cobro_eCRM(db)
            input("Presione Enter para continuar...")
        elif opcion == "4":
            os.system('cls')
            export_fichero_Transfermovil_eCRM(db)
            input("Presione Enter para continuar...")
        elif opcion == "5":
            os.system('cls')
            descarga_fichero_banco_eCRM(db)
            input("Presione Enter para continuar...")
        elif opcion == "6":
            os.system('cls')
            crea_tablas_old_debt_comercial_eCRM(db)
            input("Presione Enter para continuar...")
        elif opcion == "7":
            os.system('cls')
            concilia_cobros_transfermovil_eCRM(db)
            input("Presione Enter para continuar...")
        elif opcion == "8":
            os.system('cls')
            concilia_cobros_semanales_transfermovil_eCRM(db)
            input("Presione Enter para continuar...")
        elif opcion == "9":
            os.system('cls')
            ejecuta_todos_procedimientos(db)
            input("Presione Enter para continuar...")
        elif opcion == "s":
            os.system('cls')
            print("Fin del programa")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

            
def ejecuta_todos_procedimientos(db):
    # Aquí puedes llamar a todas las funciones necesarias en orden
    problemas_cola(db)
    actualiza_estado_de_cuenta_eCRM(db)
    cierra_gestiones_de_cobro_eCRM(db)
    export_fichero_Transfermovil_eCRM(db)
    descarga_fichero_banco_eCRM(db)
    crea_tablas_old_debt_comercial_eCRM(db)
    concilia_cobros_transfermovil_eCRM(db)
    concilia_cobros_semanales_transfermovil_eCRM(db)

# Asegúrate de definir aquí tus funciones específicas (problemas_cola, actualiza_estado_de_cuenta_eCRM, etc.)
# y también inicializar tu variable db si es necesario antes de llamar a menu_principal().

menu_principal()


