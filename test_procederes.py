import pytest
from unittest.mock import MagicMock
from pymongo.collection import Collection
from procederes import problemas_cola, actualiza_estado_de_cuenta_eCRM  # Reemplaza 'procederes' con el nombre real de tu script

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

def test_actualiza_estado_de_cuenta_eCRM(mocker) -> None:
    """
    Prueba que la función actualiza_estado_de_cuenta_eCRM actualice correctamente los documentos.

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para el resultado de update_many
    mock_update_result = mocker.MagicMock()
    mock_update_result.modified_count = 5

    # Crear un mock para la colección 'trace_process'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.update_many.return_value = mock_update_result

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = actualiza_estado_de_cuenta_eCRM(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 5
    mock_db.get_collection.assert_called_once_with('trace_process')
    mock_collection.update_many.assert_called_once_with(
        {"insert_sgc_account_state": {"$regex": "\"true\"", "$options": "i"}},
        {"$set": {"insert_sgc_account_state": "false"}}
    )

def test_actualiza_estado_de_cuenta_eCRM_no_match(mocker) -> None:
    """
    Prueba que la función actualiza_estado_de_cuenta_eCRM devuelva 0 cuando no hay documentos para actualizar.

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para el resultado de update_many
    mock_update_result = mocker.MagicMock()
    mock_update_result.modified_count = 0

    # Crear un mock para la colección 'trace_process'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.update_many.return_value = mock_update_result

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = actualiza_estado_de_cuenta_eCRM(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 0
    mock_db.get_collection.assert_called_once_with('trace_process')
    mock_collection.update_many.assert_called_once_with(
        {"insert_sgc_account_state": {"$regex": "\"true\"", "$options": "i"}},
        {"$set": {"insert_sgc_account_state": "false"}}
    )