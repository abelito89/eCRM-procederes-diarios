import pytest
from unittest.mock import MagicMock
from pymongo import MongoClient
from pymongo.collection import Collection
from procederes import concilia_cobros_transfermovil_eCRM, concilia_cobros_semanales_transfermovil_eCRM, problemas_cola, actualiza_estado_de_cuenta_eCRM, cierra_gestiones_de_cobro_eCRM, export_fichero_Transfermovil_eCRM, descarga_fichero_banco_eCRM, crea_tablas_old_debt_comercial_eCRM  # Reemplaza 'procederes' con el nombre real de tu script

def test_problemas_cola(mocker) -> None:
    """
    Prueba que la función problemas_cola devuelva la cantidad correcta de documentos con source_type "TRANSFER".

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para la colección 'payment_extern_operation'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.find.return_value.count.return_value = 10

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = problemas_cola(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 10
    mock_db.get_collection.assert_called_once_with('payment_extern_operation')
    mock_collection.find.assert_called_once_with({"source_type": "TRANSFER"})

def test_problemas_cola_no_transfer(mocker) -> None:
    """
    Prueba que la función problemas_cola devuelva 0 cuando no hay documentos con source_type "TRANSFER".

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para la colección 'payment_extern_operation'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.find.return_value.count.return_value = 0

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = problemas_cola(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 0
    mock_db.get_collection.assert_called_once_with('payment_extern_operation')
    mock_collection.find.assert_called_once_with({"source_type": "TRANSFER"})


@pytest.fixture
def mock_mongo_client():
    """Crea un cliente mock de MongoDB."""
    client = MagicMock(__spec__=MongoClient)
    return client

@pytest.fixture
def mock_database(mock_mongo_client):
    """Crea una base de datos mock."""
    # Asumiendo que 'test_db' es el nombre de la base de datos que deseas simular
    db = MagicMock()
    mock_mongo_client.test_db = db
    db.get_collection.return_value = MagicMock()
    return db

@pytest.fixture
def mock_trace_process_collection(mock_database):
    """Crea una colección mock."""
    # Asumiendo que 'trace_process' es el nombre de la colección que deseas simular
    collection = mock_database.get_collection('trace_process')
    return collection
        
def test_actualiza_estado_de_cuenta_eCRM(mock_trace_process_collection, mock_database) -> None:
    """
    Prueba que actualiza_estado_de_cuenta_eCRM actualice correctamente los documentos cuando hay documentos que actualizar.

    Args:
        mock_trace_process_collection: El fixture de mock para la colección trace_process.
        mock_database: El fixture de mock para la base de datos.
    """
    # Preparar datos de prueba
    mock_trace_process_collection.count.return_value = 1
    
    # Llamar a la función
    result = actualiza_estado_de_cuenta_eCRM(mock_database)
    
    # Verificar el resultado
    assert result == 1, "El número de documentos actualizados no coincide con lo esperado."
    mock_trace_process_collection.update_many.assert_called_once_with(
        {"insert_sgc_account_state": True},
        {"$set":{"insert_sgc_account_state": False}}
    )


def test_actualiza_estado_de_cuenta_eCRM_no_documents(mock_trace_process_collection, mock_database) -> None:
    """
    Prueba que actualiza_estado_de_cuenta_eCRM no actualice documentos cuando no hay documentos que actualizar.

    Args:
        mock_trace_process_collection: El fixture de mock para la colección trace_process.
        mock_database: El fixture de mock para la base de datos.
    """
    # Preparar datos de prueba para el caso donde no se encuentran documentos
    mock_trace_process_collection.count.return_value = 0

    # Llamar a la función
    result = actualiza_estado_de_cuenta_eCRM(mock_database)

    # Verificar el resultado
    assert result == 0, "El número de documentos actualizados no coincide con lo esperado."
    mock_trace_process_collection.update_many.assert_called_once_with(
        {"insert_sgc_account_state": True},
        {"$set": {"insert_sgc_account_state": False}}
    )

def test_cierra_gestiones_de_cobro_eCRM(mock_trace_process_collection, mock_database) -> None:
    """
    Prueba que cierra_gestiones_de_cobro_eCRM actualice correctamente los documentos cuando hay documentos que actualizar.

    Args:
        mock_trace_process_collection: El fixture de mock para la colección trace_process.
        mock_database: El fixture de mock para la base de datos.
    """

    # Preparar datos de prueba
    mock_trace_process_collection.count.return_value = 1
    
    # Llamar a la función
    result = cierra_gestiones_de_cobro_eCRM(mock_database)
    
    # Verificar el resultado
    assert result == 1, "El número de documentos actualizados no coincide con lo esperado."
    mock_trace_process_collection.update_many.assert_called_once_with(
        {"get_service_to_call_data_from_sgc": True},
        {"$set":{"get_service_to_call_data_from_sgc": False}}
    )


def test_cierra_gestiones_de_cobro_eCRM_no_documents(mock_trace_process_collection, mock_database) -> None:
    """
    Prueba que cierra_gestiones_de_cobro_eCRM no actualice documentos cuando no hay documentos que actualizar.

    Args:
        mock_trace_process_collection: El fixture de mock para la colección trace_process.
        mock_database: El fixture de mock para la base de datos.
    """
    # Preparar datos de prueba para el caso donde no se encuentran documentos
    mock_trace_process_collection.count.return_value = 0

    # Llamar a la función
    result = cierra_gestiones_de_cobro_eCRM(mock_database)

    # Verificar el resultado
    assert result == 0, "El número de documentos actualizados no coincide con lo esperado."
    mock_trace_process_collection.update_many.assert_called_once_with(
        {"get_service_to_call_data_from_sgc": True},
        {"$set": {"get_service_to_call_data_from_sgc": False}}
    )


def test_export_fichero_Transfermovil_eCRM(mock_trace_process_collection, mock_database) -> None:
    """
    Prueba que export_fichero_Transfermovil_eCRM actualice correctamente los documentos cuando hay documentos que actualizar.

    Args:
        mock_trace_process_collection: El fixture de mock para la colección trace_process.
        mock_database: El fixture de mock para la base de datos.
    """

    # Preparar datos de prueba
    mock_trace_process_collection.count.return_value = 1
    
    # Llamar a la función
    result = export_fichero_Transfermovil_eCRM(mock_database)
    
    # Verificar el resultado
    assert result == 1, "El número de documentos actualizados no coincide con lo esperado."
    mock_trace_process_collection.update_many.assert_called_once_with(
        {"export_tranfermovil_operation": True},
        {"$set":{"export_tranfermovil_operation": False}}
    )


def test_export_fichero_Transfermovil_eCRM_no_documents(mock_trace_process_collection, mock_database) -> None:
    """
    Prueba que export_fichero_Transfermovil_eCRM no actualice documentos cuando no hay documentos que actualizar.

    Args:
        mock_trace_process_collection: El fixture de mock para la colección trace_process.
        mock_database: El fixture de mock para la base de datos.
    """

    # Preparar datos de prueba para el caso donde no se encuentran documentos
    mock_trace_process_collection.count.return_value = 0

    # Llamar a la función
    result = export_fichero_Transfermovil_eCRM(mock_database)

    # Verificar el resultado
    assert result == 0, "El número de documentos actualizados no coincide con lo esperado."
    mock_trace_process_collection.update_many.assert_called_once_with(
        {"export_tranfermovil_operation": True},
        {"$set": {"export_tranfermovil_operation": False}}
    )


def test_crea_tablas_old_debt_comercial_eCRM(mock_trace_process_collection, mock_database) -> None:
    """
    Prueba que crea_tablas_old_debt_comercial_eCRM actualice correctamente los documentos cuando hay documentos que actualizar.

    Args:
        mock_trace_process_collection: El fixture de mock para la colección trace_process.
        mock_database: El fixture de mock para la base de datos
    """

    # Preparar datos de prueba
    mock_trace_process_collection.count.return_value = 1
    
    # Llamar a la función
    result = crea_tablas_old_debt_comercial_eCRM(mock_database)
    
    # Verificar el resultado
    assert result == 1, "El número de documentos actualizados no coincide con lo esperado."
    mock_trace_process_collection.update_many.assert_called_once_with(
        {"created_old_debt": True},
        {"$set":{"created_old_debt": False}}
    )


def test_crea_tablas_old_debt_comercial_eCRM_no_documents(mock_trace_process_collection, mock_database) -> None:
    """
    Prueba que crea_tablas_old_debt_comercial_eCRM no actualice los documentos cuando no hay documentos que actualizar.

    Args:
        mock_trace_process_collection: El fixture de mock para la colección trace_process.
        mock_database: El fixture de mock para la base de datos
    """
    # Preparar datos de prueba para el caso donde no se encuentran documentos
    mock_trace_process_collection.count.return_value = 0

    # Llamar a la función
    result = crea_tablas_old_debt_comercial_eCRM(mock_database)

    # Verificar el resultado
    assert result == 0, "El número de documentos actualizados no coincide con lo esperado."
    mock_trace_process_collection.update_many.assert_called_once_with(
        {"created_old_debt": True},
        {"$set": {"created_old_debt": False}}
    )


def test_concilia_cobros_transfermovil_eCRM(mock_trace_process_collection, mock_database) -> None:
    """
    Prueba que concilia_cobros_transfermovil_eCRM actualice correctamente los documentos cuando hay documentos que actualizar.

    Args:
        mock_trace_process_collection: El fixture de mock para la colección trace_process.
        mock_database: El fixture de mock para la base de datos.
    """
    # Preparar datos de prueba
    mock_trace_process_collection.count.return_value = 1
    
    # Llamar a la función
    result = concilia_cobros_transfermovil_eCRM(mock_database)
    
    # Verificar el resultado
    assert result == 1, "El número de documentos actualizados no coincide con lo esperado."
    mock_trace_process_collection.update_many.assert_called_once_with(
        {"daily_conciliation_transfer_payments": True},
        {"$set":{"daily_conciliation_transfer_payments": False}}
    )


def test_concilia_cobros_transfermovil_eCRM_no_documents(mock_trace_process_collection, mock_database) -> None:
    """
    Prueba que concilia_cobros_transfermovil_eCRM no actualice documentos cuando no hay documentos que actualizar.

    Args:
        mock_trace_process_collection: El fixture de mock para la colección trace_process.
        mock_database: El fixture de mock para la base de datos.
    """
    # Preparar datos de prueba para el caso donde no se encuentran documentos
    mock_trace_process_collection.count.return_value = 0

    # Llamar a la función
    result = concilia_cobros_transfermovil_eCRM(mock_database)

    # Verificar el resultado
    assert result == 0, "El número de documentos actualizados no coincide con lo esperado."
    mock_trace_process_collection.update_many.assert_called_once_with(
        {"daily_conciliation_transfer_payments": True},
        {"$set": {"daily_conciliation_transfer_payments": False}}
    )

def test_concilia_cobros_semanales_transfermovil_eCRM(mock_trace_process_collection, mock_database) -> None:
    """
    Prueba que concilia_cobros_semanales_transfermovil_eCRM actualice correctamente los documentos cuando hay documentos que actualizar.

    Args:
        mock_trace_process_collection: El fixture de mock para la colección trace_process.
        mock_database: El fixture de mock para la base de datos.
    """
    # Preparar datos de prueba
    mock_trace_process_collection.count.return_value = 1
    
    # Llamar a la función
    result = concilia_cobros_semanales_transfermovil_eCRM(mock_database)
    
    # Verificar el resultado
    assert result == 1, "El número de documentos actualizados no coincide con lo esperado."
    mock_trace_process_collection.update_many.assert_called_once_with(
        {"weekly_conciliation_transfer_payments": True},
        {"$set":{"weekly_conciliation_transfer_payments": False}}
    )


def test_concilia_cobros_semanales_transfermovil_eCRM_no_documents(mock_trace_process_collection, mock_database) -> None:
    """
    Prueba que concilia_cobros_semanales_transfermovil_eCRM no actualice documentos cuando no hay documentos que actualizar.

    Args:
        mock_trace_process_collection: El fixture de mock para la colección trace_process.
        mock_database: El fixture de mock para la base de datos.
    """
    # Preparar datos de prueba para el caso donde no se encuentran documentos
    mock_trace_process_collection.count.return_value = 0

    # Llamar a la función
    result = concilia_cobros_semanales_transfermovil_eCRM(mock_database)

    # Verificar el resultado
    assert result == 0, "El número de documentos actualizados no coincide con lo esperado."
    mock_trace_process_collection.update_many.assert_called_once_with(
        {"weekly_conciliation_transfer_payments": True},
        {"$set": {"weekly_conciliation_transfer_payments": False}}
    )


