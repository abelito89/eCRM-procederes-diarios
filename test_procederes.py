import pytest
from unittest.mock import MagicMock
from pymongo import MongoClient
from procederes import problemas_cola, actualiza_estado_de_cuenta_eCRM  # Asegúrate de reemplazar 'your_script' con el nombre de tu script

def test_problemas_cola():
    # Crear un mock para la base de datos
    db = MagicMock(spec=MongoClient)
    collection_mock = MagicMock()
    db.__getitem__.return_value = collection_mock
    collection_mock.find.return_value.count.return_value = 5

    # Llamar a la función con el mock
    result = problemas_cola(db)

    # Verificar que la función hizo lo que esperábamos
    db.__getitem__.assert_called_once_with('payment_extern_operation')
    collection_mock.find.assert_called_once_with({"source_type" : "TRANSFER"})
    assert result == 5

def test_actualiza_estado_de_cuenta_eCRM():
    # Crear un mock para la base de datos
    db = MagicMock(spec=MongoClient)
    collection_mock = MagicMock()
    db.__getitem__.return_value = collection_mock
    collection_mock.update_many.return_value.modified_count = 10

    # Llamar a la función con el mock
    result = actualiza_estado_de_cuenta_eCRM(db)

    # Verificar que la función hizo lo que esperábamos
    db.__getitem__.assert_called_once_with('trace_process')
    collection_mock.update_many.assert_called_once_with(
        {"insert_sgc_account_state": {"$regex": "\"true\"", "$options" : "i"}},
        {"$set": {"insert_sgc_account_state": "false"}}
    )
    assert result == 10
