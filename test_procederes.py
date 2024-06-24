import pytest
from unittest.mock import MagicMock
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


def test_actualiza_estado_de_cuenta_eCRM(mocker) -> None:
    """
    Prueba que la función actualiza_estado_de_cuenta_eCRM actualice correctamente los documentos.

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para la colección 'trace_process'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.count.return_value = 5

    # Crear un mock para el resultado de update_many
    mock_update_result = mocker.MagicMock()
    mock_collection.update_many.return_value = mock_update_result

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = actualiza_estado_de_cuenta_eCRM(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 5
    mock_db.get_collection.assert_called_once_with('trace_process')
    mock_collection.count.assert_called_once_with({"insert_sgc_account_state": True})
    mock_collection.update_many.assert_called_once_with(
        {"insert_sgc_account_state": True},
        {"$set": {"insert_sgc_account_state": False}}
    )

def test_actualiza_estado_de_cuenta_eCRM_no_match(mocker) -> None:
    """
    Prueba que la función actualiza_estado_de_cuenta_eCRM devuelva 0 cuando no hay documentos para actualizar.

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para la colección 'trace_process'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.count.return_value = 0

    # Crear un mock para el resultado de update_many
    mock_update_result = mocker.MagicMock()
    mock_collection.update_many.return_value = mock_update_result

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = actualiza_estado_de_cuenta_eCRM(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 0
    mock_db.get_collection.assert_called_once_with('trace_process')
    mock_collection.count.assert_called_once_with({"insert_sgc_account_state": True})
    mock_collection.update_many.assert_called_once_with(
        {"insert_sgc_account_state": True},
        {"$set": {"insert_sgc_account_state": False}}
    )


def test_cierra_gestiones_de_cobro_eCRM(mocker) -> None:
    """
    Prueba que la función cierra_gestiones_de_cobro_eCRM actualice correctamente los documentos.

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para la colección 'trace_process'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.count.return_value = 5

    # Crear un mock para el resultado de update_many
    mock_update_result = mocker.MagicMock()
    mock_collection.update_many.return_value = mock_update_result

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = cierra_gestiones_de_cobro_eCRM(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 5
    mock_db.get_collection.assert_called_once_with('trace_process')
    mock_collection.count.assert_called_once_with({"get_service_to_call_data_from_sgc": True})
    mock_collection.update_many.assert_called_once_with(
        {"get_service_to_call_data_from_sgc": True},
        {"$set": {"get_service_to_call_data_from_sgc": False}}
    )

def test_cierra_gestiones_de_cobro_eCRM_no_match(mocker) -> None:
    """
    Prueba que la función cierra_gestiones_de_cobro_eCRM devuelva 0 cuando no hay documentos para actualizar.

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para la colección 'trace_process'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.count.return_value = 0

    # Crear un mock para el resultado de update_many
    mock_update_result = mocker.MagicMock()
    mock_collection.update_many.return_value = mock_update_result

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = cierra_gestiones_de_cobro_eCRM(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 0
    mock_db.get_collection.assert_called_once_with('trace_process')
    mock_collection.count.assert_called_once_with({"get_service_to_call_data_from_sgc": True})
    mock_collection.update_many.assert_called_once_with(
        {"get_service_to_call_data_from_sgc": True},
        {"$set": {"get_service_to_call_data_from_sgc": False}}
    )


def test_export_fichero_Transfermovil_eCRM(mocker) -> None:
    """
    Prueba que la función export_fichero_Transfermovil_eCRM actualice correctamente los documentos.

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para la colección 'trace_process'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.count.return_value = 5

    # Crear un mock para el resultado de update_many
    mock_update_result = mocker.MagicMock()
    mock_collection.update_many.return_value = mock_update_result

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = export_fichero_Transfermovil_eCRM(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 5
    mock_db.get_collection.assert_called_once_with('trace_process')
    mock_collection.count.assert_called_once_with({"export_tranfermovil_operation": True})
    mock_collection.update_many.assert_called_once_with(
        {"export_tranfermovil_operation": True},
        {"$set": {"export_tranfermovil_operation": False}}
    )

def test_export_fichero_Transfermovil_eCRM_no_match(mocker) -> None:
    """
    Prueba que la función export_fichero_Transfermovil_eCRM devuelva 0 cuando no hay documentos para actualizar.

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para la colección 'trace_process'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.count.return_value = 0

    # Crear un mock para el resultado de update_many
    mock_update_result = mocker.MagicMock()
    mock_collection.update_many.return_value = mock_update_result

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = export_fichero_Transfermovil_eCRM(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 0
    mock_db.get_collection.assert_called_once_with('trace_process')
    mock_collection.count.assert_called_once_with({"export_tranfermovil_operation": True})
    mock_collection.update_many.assert_called_once_with(
        {"export_tranfermovil_operation": True},
        {"$set": {"export_tranfermovil_operation": False}}
    )


def test_descarga_fichero_banco_eCRM(mocker) -> None:
    """
    Prueba que la función descarga_fichero_banco_eCRM actualice correctamente los documentos.

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para la colección 'trace_process'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.count.return_value = 5

    # Crear un mock para el resultado de update_many
    mock_update_result = mocker.MagicMock()
    mock_collection.update_many.return_value = mock_update_result

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = descarga_fichero_banco_eCRM(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 5
    mock_db.get_collection.assert_called_once_with('trace_process')
    mock_collection.count.assert_called_once_with({"insert_in_mongo_ftp_files": True})
    mock_collection.update_many.assert_called_once_with(
        {"insert_in_mongo_ftp_files": True},
        {"$set": {"insert_in_mongo_ftp_files": False}}
    )

def test_descarga_fichero_banco_eCRM_no_match(mocker) -> None:
    """
    Prueba que la función descarga_fichero_banco_eCRM devuelva 0 cuando no hay documentos para actualizar.

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para la colección 'trace_process'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.count.return_value = 0

    # Crear un mock para el resultado de update_many
    mock_update_result = mocker.MagicMock()
    mock_collection.update_many.return_value = mock_update_result

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = descarga_fichero_banco_eCRM(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 0
    mock_db.get_collection.assert_called_once_with('trace_process')
    mock_collection.count.assert_called_once_with({"insert_in_mongo_ftp_files": True})
    mock_collection.update_many.assert_called_once_with(
        {"insert_in_mongo_ftp_files": True},
        {"$set": {"insert_in_mongo_ftp_files": False}}
    )


def test_crea_tablas_old_debt_comercial_eCRM(mocker) -> None:
    """
    Prueba que la función crea_tablas_old_debt_comercial_eCRM actualice correctamente los documentos.

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para la colección 'trace_process'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.count.return_value = 5

    # Crear un mock para el resultado de update_many
    mock_update_result = mocker.MagicMock()
    mock_collection.update_many.return_value = mock_update_result

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = crea_tablas_old_debt_comercial_eCRM(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 5
    mock_db.get_collection.assert_called_once_with('trace_process')
    mock_collection.count.assert_called_once_with({"created_old_debt": True})
    mock_collection.update_many.assert_called_once_with(
        {"created_old_debt": True},
        {"$set": {"created_old_debt": False}}
    )

def test_crea_tablas_old_debt_comercial_eCRM_no_match(mocker) -> None:
    """
    Prueba que la función crea_tablas_old_debt_comercial_eCRM devuelva 0 cuando no hay documentos para actualizar.

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para la colección 'trace_process'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.count.return_value = 0

    # Crear un mock para el resultado de update_many
    mock_update_result = mocker.MagicMock()
    mock_collection.update_many.return_value = mock_update_result

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = crea_tablas_old_debt_comercial_eCRM(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 0
    mock_db.get_collection.assert_called_once_with('trace_process')
    mock_collection.count.assert_called_once_with({"created_old_debt": True})
    mock_collection.update_many.assert_called_once_with(
        {"created_old_debt": True},
        {"$set": {"created_old_debt": False}}
    )


def test_concilia_cobros_transfermovil_eCRM(mocker) -> None:
    """
    Prueba que la función concilia_cobros_transfermovil_eCRM actualice correctamente los documentos.

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para la colección 'trace_process'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.count.return_value = 5

    # Crear un mock para el resultado de update_many
    mock_update_result = mocker.MagicMock()
    mock_collection.update_many.return_value = mock_update_result

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = concilia_cobros_transfermovil_eCRM(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 5
    mock_db.get_collection.assert_called_once_with('trace_process')
    mock_collection.count.assert_called_once_with({"daily_conciliation_transfer_payments": True})
    mock_collection.update_many.assert_called_once_with(
        {"daily_conciliation_transfer_payments": True},
        {"$set": {"daily_conciliation_transfer_payments": False}}
    )

def test_concilia_cobros_transfermovil_eCRM_no_match(mocker) -> None:
    """
    Prueba que la función concilia_cobros_transfermovil_eCRM devuelva 0 cuando no hay documentos para actualizar.

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para la colección 'trace_process'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.count.return_value = 0

    # Crear un mock para el resultado de update_many
    mock_update_result = mocker.MagicMock()
    mock_collection.update_many.return_value = mock_update_result

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = concilia_cobros_transfermovil_eCRM(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 0
    mock_db.get_collection.assert_called_once_with('trace_process')
    mock_collection.count.assert_called_once_with({"daily_conciliation_transfer_payments": True})
    mock_collection.update_many.assert_called_once_with(
        {"daily_conciliation_transfer_payments": True},
        {"$set": {"daily_conciliation_transfer_payments": False}}
    )


def test_concilia_cobros_semanales_transfermovil_eCRM(mocker) -> None:
    """
    Prueba que la función concilia_cobros_transfermovil_eCRM actualice correctamente los documentos.

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para la colección 'trace_process'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.count.return_value = 5

    # Crear un mock para el resultado de update_many
    mock_update_result = mocker.MagicMock()
    mock_collection.update_many.return_value = mock_update_result

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = concilia_cobros_transfermovil_eCRM(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 5
    mock_db.get_collection.assert_called_once_with('trace_process')
    mock_collection.count.assert_called_once_with({"weekly_conciliation_transfer_payments": True})
    mock_collection.update_many.assert_called_once_with(
        {"weekly_conciliation_transfer_payments": True},
        {"$set": {"weekly_conciliation_transfer_payments": False}}
    )

def test_concilia_cobros_semanales_transfermovil_eCRM_no_match(mocker) -> None:
    """
    Prueba que la función concilia_cobros_transfermovil_eCRM devuelva 0 cuando no hay documentos para actualizar.

    Args:
        mocker: El fixture de mock de pytest para crear objetos mock.
    """
    # Crear un mock para la colección 'trace_process'
    mock_collection = mocker.MagicMock(spec=Collection)
    mock_collection.count.return_value = 0

    # Crear un mock para el resultado de update_many
    mock_update_result = mocker.MagicMock()
    mock_collection.update_many.return_value = mock_update_result

    # Crear un mock para la base de datos
    mock_db = mocker.MagicMock()
    mock_db.get_collection.return_value = mock_collection

    # Ejecutar la función con el mock de la base de datos
    result = concilia_cobros_transfermovil_eCRM(mock_db)

    # Verificar que el resultado sea el esperado
    assert result == 0
    mock_db.get_collection.assert_called_once_with('trace_process')
    mock_collection.count.assert_called_once_with({"weekly_conciliation_transfer_payments": True})
    mock_collection.update_many.assert_called_once_with(
        {"weekly_conciliation_transfer_payments": True},
        {"$set": {"weekly_conciliation_transfer_payments": False}}
    )