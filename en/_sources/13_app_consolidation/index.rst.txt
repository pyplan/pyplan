=============================
Consolidación de aplicaciones
=============================

Introducción
============

En esta sección se detalla cómo es posible incorporar (consolidar) reglas de negocio, interfaces y archivos desde una versión de una aplicación a la versión abierta.

.. figure:: images/section.png

Elección de aplicación y versión fuente
=======================================

En este paso se elige la aplicación y la versión desde la cual se importarán los nuevos cambios a la versión abierta actual.

.. figure:: images/step1.png

----------
Parámetros
----------
- App path: ubicación de la aplicación fuente. Al hacer click en el campo, se desplegará una ventana para navegar las carpetas del sistema y elegir la aplicación deseada.
- Version: versión de la aplicación fuente desde la cual se quiere incorporar nuevos cambios.
- Business rules - Modules: selector para elegir los módulos que se quieren incorporar.
- Business rules - Replace matching nodes outside these modules: esta opción es relevante si dentro de los módulos elegidos para consolidar existe un nodo con un identifier que coincide con el identifier de un nodo de la versión de destino (actual), pero que en esta última se encuentra en otro módulo por fuera de los módulos elegidos para consolidar. En caso de estar tildada la opción, las propiedades de estos nodos serán reemplazados por los nuevos nodos. En caso de estar destildada, los nodos en cuestión nuevos serán renombrados con el sufijo "_new" luego de la consolidación.
- Interfaces: selector para elegir qué interfaces se quieren incorporar.
- Files: si esta opción está tildada, se compararán todos los archivos dentro de la versión fuente vs. los archivos dentro de la versión de destino.
- Version metadata: si esta opción está tildada, se comparará el archivo metadata.json dentro de la versión fuente vs. la de destino.

Al hacer click en el botón "Next", Pyplan calculará las diferencias entre la versión fuente vs. la de destino y las mostrará en el siguiente paso.

Comparación y elección de diferencias a aplicar
===============================================

En este paso se visualizarán las diferencias entre la versión fuente y la versión actual abierta.

.. figure:: images/step2.png

------------------------------------
Listado de elementos con diferencias
------------------------------------
Del lado izquierdo se muestran los nodos, interfaces y archivos en los que existen diferencias entre las dos versiones.

.. figure:: images/step2-left.png

Los elementos tildados serán los que efectivamente se aplicarán al confirmar los cambios.

Significado de íconos por color
-------------------------------
.. figure:: images/step2-icons.png

- Verde: nuevo elemento que será agregado.
- Amarillo: elemento existente que será modificado.
- Rojo: elemento que será eliminado

-------------------------------
Comparación de elemento elegido
-------------------------------
Del lado derecho se muestran las diferencias del elemento elegido. Lo que se muestra bajo "Old" son las propiedades de la versión abierta actual. Lo que se muestra bajo "New", las de la versión fuente. De confirmarse el cambio, se aplicarán las propiedades que se visualizan bajo "New".

.. figure:: images/step2-right.png

En caso de elegir un elemento de Business rules, las diferencias se presentan en dos pestañas:

- Properties: muestra las propiedades del nodo como el título, posición en diagrama (x, y), tamaño (w, h), entre otros.
- Definition: muestra la definición del nodo (el código Python).

Para el resto de los elementos (Interfaces, Files y Version metadata), sólo se muestran diferencias bajo la pestaña de Properties.

-----------------------
Confirmación de cambios
-----------------------
Al hacer click en el botón "Confirm", se aplicarán los cambios elegidos.

Consideraciones:

- Los cambios aplicados en **Files y Version metadata** son **irreversibles**.
- Los cambios en **Business rules e Interfaces pueden ser revertidos** si no se guardan los cambios en la aplicación.

Resumen de consolidación
========================
En esta sección es posible ver un resumen de los cambios aplicados en la versión abierta actual.

.. figure:: images/step3.png

Los cambios aplicados en Files y Version metadata son definitivos. Los cambios en Business rules e Interfaces serán grabados si se guarda la aplicación.

Base de datos con cambios aplicados
===================================
En la carpeta de la versión, luego de aplicada una consolidación, se registran todos los cambios aplicados en un archivo llamado "consolidations.db".

Tener en cuenta que si los cambios en Business rules o Interfaces no se guardan finalmente en la aplicación, igualmente quedarán impactados en la base de datos.
