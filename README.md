
# Automatización de procederes diarios de Soporte de eCRM ETECSA

Este proyecto contiene un conjunto de scripts en Python que interactúan con una base de datos MongoDB para automatizar varios procesos de gestión en un sistema de eCRM (Customer Relationship Management). Los scripts permiten realizar tareas como actualización de estados, conciliación de pagos y descarga de archivos, entre otros.

## Requisitos

- Python 3.6+
- MongoDB
- Paquetes Python: pymongo, python-dotenv, dnspython, unittest, pytest

## Instalación

1. Clona este repositorio en tu máquina local:
   
```bash
git clone https://github.com/abelito89/eCRM-procederes-diarios.git
```

2. Crea un entorno virtual y actívalo:


```bash
python3 -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Crea un archivo .env en la raíz del proyecto con la siguiente línea, reemplazando your_mongodb_connection_string con la cadena de conexión a tu servidor de MongoDB:

```plaintext
SERVER=your_mongodb_connection_string
```

## Uso
### Ejecución del Menú Principal
Para ejecutar el menú principal y seleccionar las diferentes opciones manualmente, ejecuta:

```bash
python main.py
```

### Opciones del Menú
1. Problemas en cola de pagos y recargas de terceros: Calcula y muestra la cantidad de problemas en la cola de pagos y recargas de terceros basándose en el tipo de fuente 'TRANSFER'.

2. Actualización de estado de cuenta eCRM: Actualiza el valor del campo 'insert_sgc_account_state' a 'false' en todos los documentos donde este campo contiene el valor 'true'.

3. Cierre de gestiones de cobro eCRM: Actualiza el valor del campo 'get_service_to_call_data_from_sgc' a 'false' en todos los documentos donde este campo contiene el valor 'true'.

4. Exportación de fichero Transfermovil eCRM: Actualiza el valor del campo 'export_tranfermovil_operation' a 'false' en todos los documentos donde este campo contiene el valor 'true'.

5. Descarga de fichero banco eCRM: Actualiza el valor del campo 'insert_in_mongo_ftp_files' a 'false' en todos los documentos donde este campo contiene el valor 'true'.

6. Creación de tablas de edad de deuda comercial eCRM: Actualiza el valor del campo 'created_old_debt' a 'false' en todos los documentos donde este campo contiene el valor 'true'.

7. Conciliación de cobros diarios Transfermovil eCRM: Actualiza el valor del campo 'daily_conciliation_transfer_payments' a 'false' en todos los documentos donde este campo contiene el valor 'true'.

8. Conciliación de cobros semanales Transfermovil eCRM: Actualiza el valor del campo 'weekly_conciliation_transfer_payments' a 'false' en todos los documentos donde este campo contiene el valor 'true'.

9. Ejecutar todos los procedimientos: Ejecuta todas las funciones mencionadas anteriormente en secuencia.

## Pruebas
Las pruebas para cada función están incluidas en el archivo test_script.py. Estas pruebas utilizan pytest y unittest.mock para verificar el correcto funcionamiento de las funciones sin necesidad de una conexión real a MongoDB.

Ejecución de Pruebas
Para ejecutar las pruebas, asegúrate de tener pytest instalado y ejecuta el siguiente comando en la raíz del proyecto:


```bash
pytest
```

Este archivo README.md proporciona una guía completa sobre cómo configurar y utilizar los scripts de automatización para el sistema eCRM. Asegúrate de seguir cada paso cuidadosamente para configurar el entorno y ejecutar las tareas correctamente.