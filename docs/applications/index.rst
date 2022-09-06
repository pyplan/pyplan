Aplicaciones
===================
=================================
Características de una aplicación
=================================

Una aplicación en Pyplan es un desarrollo particular que utiliza las funcionalidades que brinda la plataforma para atender un problema específico.

Una aplicación puede estar compuesta por diversos elementos, entre los que se encuentran:

.. list
* Lectura de fuentes de datos externas.
* Formularios de carga de datos.
* Módulos de cálculo y procesamiento.
* Interfaces de visualización.


Estos elementos son almacenados en un espacio de trabajo.

| Todos los usuarios tienen como mínimo acceso a dos espacios de trabajo:
.. list
* Un espacio público denominado **"Public"** donde se comparten aplicaciones accesibles para todos los usuarios.
* Un espacio Privado denominado **"My Workspace"**, donde cada usuario puede crear o modificar aplicaciones en un ambiente solo accesible para él mismo.
| Además, los usuarios tienen acceso a espacios de trabajos de equipos a los que pertenecen: **"Teams"**. Estos equipos son la forma de compartir información con restricción de acceso a determinados usuarios.


===================
Equipos de trabajo
===================
Los equipos de trabajos son creados por el administrador del sistema y los permisos de acceso otorgados por **"Departamento"** al que pertenece un usuario.
Un mismo usuario puede formar parte de varios **"Departamentos"**

=============================
Administrador de aplicaciones
=============================
El administrador de aplicaciones permite navegar por las aplicaciones accesibles para cada usuario:

.. figure:: images/adm_apps.png


Ademas de crear nuevas aplicaciones, es posible realizar las siguientes acciones sobre ellas:

.. figure:: images/opciones_de_apps.png

=================================
Creación de la primera aplicación
=================================

Pyplan es un ambiente de desarrollo integrado de aplicaciones, pensado para usuarios sin conocimientos de programación.
Es por esto que la forma de construir la lógica de cálculo y procesamiento de las aplicaciones se produce a través de bloques o pasos de cálculo, representados por nodos en un diagrama de influencia.
Al hacer click en **crear una aplicación**, aparece un cuadro de diálogo que permite optar entre crear una aplicación desde cero o a partir de un ejemplo.

.. figure:: images/crear_app.png

En este caso, la aplicación de análisis de datos que se crea tiene definido inciarse mostrando un menú determinado como el que muestra la siguiente imagen:

.. figure:: images/menu_app_analisis.png

Haciendo click sobre **"View Code"** se accede al diagrama de influencia que representa los diferentes pasos de procesamiento de datos y cálculos que se realizan para generar las salidas de información.

.. figure:: images/first_diagram.png
