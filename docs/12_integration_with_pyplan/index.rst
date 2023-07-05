======================
Integración con Pyplan
======================

Introducción
============

En esta sección se detalla cómo es posible consumir datos generados en una aplicación de Pyplan desde fuera de Pyplan.

API endpoint
============

---------------------------
Creación de un API endpoint
---------------------------

Para crear un API endpoint, es necesario crear un nodo cuyo resultado sea una función de Python que, opcionalmente, puede recibir parámetros.
Por ejemplo, el código del nodo podría ser el siguiente:

.. figure:: images/function.png

Luego, hacer click derecho sobre el nodo creado y elegir la opción **"Get API Endpoint"**:

.. figure:: images/get_api_endpoint_menu_option.png

Se desplegará la siguiente ventana:

.. figure:: images/get_api_endpoint_window.png

La opción **"Share instance"** permite que múltiples llamadas al API endpoint se atiendan desde una misma instancia sin necesidad de crear una nueva por cada llamada.
Por el contrario, deshabilitando esta opción, cada llamada creara una nueva instancia en Pyplan para atenderla.
Siguiendo con el ejemplo, la URL **"https://dev.pyplan.com/api/result/f274199c-28d0-437d-b136-ec2284dcb9a8/"** será nuestro API endpoint al cual podremos llamar desde fuera de Pyplan.

----------------------------------------
Estructura de la llamada al API endpoint
----------------------------------------
- Método HTTP: POST
- Content-Type: application/json
- Headers (opcional): si el endpoint tiene asignado una Api key, se debe enviar como parámetro "x-api-key".
- Body (Opcional): form-data. Aquí se envían los parámetros para alimentar la función.

Ejemplo realizado en plataforma Postman:

.. figure:: images/postman.png

-----------------------
Gestor de API endpoints
-----------------------
En la sección **"External Link Endpoints"** es posible editar y eliminar los API endpoints creados de la aplicación actual.

.. figure:: images/external_links_manager_option.png

.. figure:: images/external_links_manager.png

Para editar un API endpoint, se debe seleccionar el enlace a editar y luego hacer click en el botón "Edit":

.. figure:: images/external_link_edit.png

Se desplegará la siguiente ventana:

.. figure:: images/external_link_edit_window.png

Opciones:

- Common instance: permite habilitar/deshabilitar el compartir la instancia al hacer múltiples llamadas.
- Active: permite habilitar/deshabilitar el API endpoint por completo.
- Custom endpoint: permite asignarle un nombre personalizado al link externo. El link final quedará disponible para copiar en el Gestor de API endpoints.
- Executor: permite elegir con qué usuario abrir la instancia.
- Api key: permite seleccionar una clave creada anteriormente que deberá enviarse como Header en la llamada al endpoint con la clave "x-api-key".

Para confirmar los cambios, se debe hacer click en el botón **"Confirm"**. Para no aplicar los cambios, hacer click en **"Cancel"**

Para borrar un API endpoint, se debe hacer click en el siguiente ícono:

.. figure:: images/external_link_delete.png

------------------
Gestor de API keys
------------------
Para crear, editar o eliminar Api keys, se debe acceder a través del botón "Show Api keys":

.. figure:: images/external_links_show_api_keys.png

Para crear una nueva Api key, hacer click en el botón "Create Api key":

.. figure:: images/external_links_api_key_create.png

Se desplegará la siguiente ventana:

.. figure:: images/external_links_api_key_create_window.png

Opciones:

- Active: permite habilitar/deshabilitar la Api key.
- Alias: permite asignarle un nombre personalizado a la Api key para que sea más fácil de reconocer al asignarla a  Api endpoints.
- Key: la clave misma. Es posible editarla por una personalizada. Guardar esta clave de manera segura ya que no será posible visualizarla luego de creada. Sólo podrá generarse una nueva o eliminarse.

Para confirmar los cambios, se debe hacer click en el botón **"Confirm"**. Para descartar la creación, hacer click en **"Cancel"**

Para editar una Api key, se debe seleccionar la Api key a editar y luego hacer click en el botón "Edit Api key":

.. figure:: images/external_links_api_key_edit.png

Se desplegará una ventana con las mismas opciones que al crear una nueva Api key.

Para borrar una Api key, se debe hacer click en el siguiente ícono:

.. figure:: images/external_links_api_key_delete.png

Para asignar una Api key a un Api endpoint, se debe editar el Api endpoint y seleccionar la Api key que se desee:

.. figure:: images/external_link_select_api_key.png

Link a interfaz
============

---------------------------
Creación de un Link a interfaz
---------------------------

Para crear un Link a interfaz, se debe ir a la sección Interfaces:

.. figure:: images/interface_links_interfaces_option.png