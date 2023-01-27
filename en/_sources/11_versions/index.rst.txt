Versiones y escenarios
======================

Una aplicación puede contener muchas versiones. Cada versión contiene la lógica, las interfaces, los escenarios, datos y definición de formularios y otros datos de entrada.

La estructura de una aplicación es la siguiente:

.. figure:: images/app_new_structure.png


Versiones
---------

------------
Introducción
------------

Al momento de crear una aplicación, se creará una versión por defecto (Default). Cada vez que el usuario abra una aplicación, siempre estará 
posicionado sobre una versión en particular que se puede visualizar el la barra superior.

Las versiones tienen múltiples propósitos y se pueden utilizar como ciclo de desarrollo, ciclos de planeamiento, etc.

.. admonition:: Uso simultáneo

   Dos usuarios pueden trabajar (y guardar cambios) al mismo tiempo en versiones **distintas** de la misma aplicación.

--------------------------
Administrador de versiones
--------------------------

Para acceder al administrador de versiones de la aplicación, debe hacer click en la opción **"Versiones"** del menú principal.

.. figure:: images/version_manager.png

Desde el administrador podrá crear, editar, exportar e importar versiones. También podrá de manera simple cambiar el estado de una versión.

Para crear una nueva versión debe hacer click en botón **"Crear versión"**. Luego se abrirá una ventana como la siguiente:

.. figure:: images/create_version.png
    
Las nuevas versiones siempre toman como base una versión existente, por lo tanto todo el contenido de la versión seleccionada como base se copiará a la nueva versión.
También puede especificar diferentes etiquetas (ingresando texto y presionando Enter). Estas etiquetas facilitarán la búsqueda de la versión.

La opción "Establecer como versión por defecto" permite especificar que la nueva versión que se está por crear será la versión que se abrirá al abrir la aplicación.

Al confirmar la creación de la nueva versión y si la opción de "Abrir luego de crear" está seleccionada, se abrirá la nueva versión y ya la podrá 
visualizar en la barra superior.


---------------------
Estado de una versión
---------------------

Cada versión puede tener alguno de los siguientes estados:

- **Activa**: la versión está en uso y puede ser modificada.
- **Cerrada**: la versión está cerrada, por lo tanto no se pueden realizar cambios en esta versión.
- **Archivada**: la versión esta cerrada y archivada. En este caso no se pueden realizar cambios y se oculta de los principales listados.



Escenarios
----------

------------
Introducción
------------

Un escenario está formado por un conjunto de resultados de determinados nodos que se almacenan con el fin de ser utilizados posteriormente para la comparación.

En una versión pueden existir muchos escenarios. Pyplan permite la comparación de escenarios incluso entre diferentes versiones de la misma aplicación.

.. admonition:: Comparación

   Para poder comparar dos o mas escenarios, los resultados a comparar deben tener la misma estructura.


---------------------------
Administrador de escenarios
---------------------------

Para acceder al administrador de escenarios, debe hacer click en la opción **"Escenarios"** del menú principal.

.. figure:: images/scenario_manager.png

Desde el administrador podrá crear, editar, exportar e importar escenarios.

Para crear un nuevo escenario debe hacer click en botón **"Crear escenario"**. Luego se abrirá una ventana como la siguiente:

.. figure:: images/create_scenario.png

Aquí deberá definir el nombre, el alias (utilizado como etiqueta para la comparación), una descripción opcional y deberá especificar los nodos 
de los cuales se guardarán los resultados. 

.. admonition:: Aclaración

   En este paso está definiendo el escenario, aunque opcionalmente también puede guardar el resultado del escenario. 
   Mas adelante veremos como puede actualizar los resultados de un escenario o generar un nuevo escenario sin necesidad de ingresar al administrador.

----------------
Grabar escenario
----------------

Una vez definido un escenario (especificando los nodos que van a persistir), puede grabar el escenario actual o crear un escenario nuevo 
haciendo click en el botón "Grabar escenario" 

.. figure:: images/create_scenario_button.png


Si selecciona la opción "Escenario existente":

.. figure:: images/save_existing_scenario.png

al confirmar, se guardarán los resultados de los nodos definidos en el escenario seleccionado, sobre-escribiendo los resultados anteriores.

Si selecciona la opción "Nuevo escenario":

.. figure:: images/save_new_scenario.png

deberá especificar el escenario que se tomará como base y asignar un nombre y alias. Al confirmar se creará un nuevo escenario con los resultados 
de los nodos que se especificaron en el escenario seleccionado como base.


-------------------------
Comparación de escenarios
-------------------------

Puede comparar diferentes escenarios (incluso de diferentes versiones) haciendo clic en el botón "Seleccionar escenarios": 

.. figure:: images/select_scenario_button.png

En la siguiente ventana podrá seleccionar los escenarios que desea comparar, indicando también cuál de estos se tomará como base para la comparación.

.. figure:: images/select_scenario_popup.png

Para que un componente (tabla o gráfico) permita la comparación de escenarios, deberá habilitar la opción de comparación desde las propiedades del componente:

.. figure:: images/compare_scenarios_properties.png

Esta opción agregará una nueva dimension "Pyplan Scenarios" la cual contendrá la lista de escenarios seleccionados.
También puede especificar si se agregan o no los campos calculados de diferencia (tanto absoluta como porcentual).
