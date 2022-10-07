=======================
Ventana de Codificación
=======================

Creación de la primera aplicación
=================================

Pyplan es un ambiente de desarrollo integrado de aplicaciones, pensado para usuarios sin conocimientos de programación.
Es por esto que la lógica de cálculo y procesamiento de datos de las aplicaciones se construye arrastrando diferentes tipos de nodos en un diagrama de influencia.

Al hacer click en **crear una aplicación**, aparece un cuadro de diálogo que permite optar entre crear una aplicación desde cero o a partir de un ejemplo.

.. figure:: images/create_appg.gif

Eligiendo crear una aplicación de análisis de datos y luego seleccionando la **visualización del código** se llega a una ventana como la siguiente:

.. figure:: images/diagrama+nodo.png
   

Elementos de la ventana de codificación
=======================================

Una vez hecho click en el icono de **código** del menú principal, se accede al diagrama de influencia:

.. figure:: images/menu_codigo_diagrama.png

Los elementos que constituyen esta sección de la plataforma son:

1. **Diagrama de influencia**: Representación gráfica del procesamiento de datos hasta su transformación en salida.
2. **Tipos de visualización de nodos**: Resultado | Código+Resultado | Código+Preview.
3. **Bot de ayuda**: Robot asistente que interpreta lenguaje natural para responder a preguntas sobre el uso de Pyplan.
4. **Atajos de Navegación**: Link a Pyplan Home y al Home de la aplicación, accesibles al hacer click sobre el logo de Pyplan y el título de la aplicación, respectivamente.
5. **Propiedades de una aplicación**: Desplegables al hacer click en los tres puntos a la derecha del título de la app.

  
----------------------
Diagrama de Influencia
----------------------

Es la representación gráfica del proceso de cálculo. 
Cada nodo representa un paso de cálculo en el proceso de transformación de los datos.
Un nodo se selecciona haciendo click sobre el mismo.
Al hacer doble-click sobre un nodo, este es calculado. Su resultado se muestra en pantalla completa de acuerdo con su configuración de visualización predeterminada.
Los vínculos (flechas) entre nodos son generados automáticamente al invocar un nodo dentro de la definición de otro.

#.. warning:: (aquí debiéramos incluir un link a una de las lecciones que te muestren paso a paso esta sección)

--------------------------
Características de un Nodo
--------------------------
Un nodo es la unidad mínima de construcción del proceso de cálculo. 
Para agregar un nodo se arrastra el mismo sobre el diagrama.

Cada nodo cuenta con las siguientes propiedades:

Título del nodo
---------------
Es el texto que se visualiza dentro del nodo en el diagrama

Id del nodo
-----------
Es el identificador del nodo, es decir, la forma en la que un nodo es invocado en la definición de otro nodo. El Id del nodo se genera automáticamente a partir del título, pero puede ser cambiado por el usuario.

Unidades
--------
En caso de que un nodo contenga una medida única, es posible indicar su unidad. Esta será mostrada entre paréntesis al lado del título al momento de mostrar los resultados del nodo. Vale destacar que las unidades solo se incluyen para ser visualizadas, no forman parte del cálculo de resultados.

.. image:: images/propiedades_grales_nodo.png
---------------------------------------------

Definición
----------
Es la operación de transformación ejecutada al evaluar un nodo. Su código esta escrito en lenguaje Python. Termina con la definición de su resultado **"result="**

Vista Previa
------------
Es la descripción técnica de la salida del proceso de cálculo.

Resultado
---------
Es el resultado que surge de ejecutar el código de la definición. Cuando este resultado es un objeto interpretado por Pyplan (un dataframe de Pandas, una matriz de Numpy, o una matriz con dimensiones designadas de Xarray), 
este puede visualizarse de forma gráfica o de tabla.

.. image:: images/nodo_def_pv_res.png

Documentación
-------------
Es el texto que describe conceptualmente cada paso de cálculo y se despliega en la parte inferior de la vista de resultados.

.. image:: images/resultado+doc.png

Entradas
--------

Listado de nodos utilizados en la definición de un nodo.

Salidas
-------

Listado de nodos que utilizan el resultado del nodo seleccionado

.. image:: images/propiedades_sa-_nodo.png

Para acceder a todas estas propiedades se puede hacer click sobre el nodo para seleccionarlo, luego click derecho o doble-click sobre él. También se visualizan las propiedades al calcular el nodo.
-------------
Tipos de Nodo
-------------

Existen diferentes tipos de nodos para diferentes propósitos. Sus funcionalidades han sido diseñadas para facilitar la definición de los parámetros necesarios para su ejecución.

.. image:: images/tipos_nodo.png


Variable
--------
Los nodos de tipo variable son los más utilizados, dado que tienen la función de contener un proceso de cálculo genérico.
Son de color azul inicialmente. En caso de que no tenga salidas, este color cambia a gris y se lo considera un reporte.
Cambia a color rojo en caso de que las salidas del nodo se encuentren fuera del módulo al que pertenece.

Lectura de datos
----------------

Nodo que al arrastrarse despliega un asistente para conectarse a distintas fuentes de datos:

.. image:: images/nodo_lectura.png

.. image:: images/asistente_csv.png

Entrada de datos
----------------
Nodo que permite crear un proceso de entrada de datos manuales. 

.. image:: images/tipo_de_ent_datos.png

Una vez elegido el tipo de entrada de datos se despliega un asistente para su configuración. En este caso se muestra el asistente para crear una 
Tabla de entrada de datos.

.. image:: images/entrada_tabla.png

Botón
-----
El boton es un nodo especial que permite ejecutar acciones sobre los nodos.

Índice
------
El nodo índice es la forma en que Pyplan almacena las dimensiones que son utilizadas a través de todo el proceso de cálculo.
Su definición conduce a la determinación de una lista de elementos que constituyen la dimensión.
Tienen un funcionamiento particular cuando se los incluye en interfaces.

Texto
-----
El cuadro de texto es un elemento de construcción del diagrama con el único fin de facilitar la interpretación del diagrama de influencia.

Módulo
------
Es un tipo de nodo especial que permite contener nodos en su interior. Sirve para organizar jerárquicamente un calculo complejo. A un módulo se ingresa haciendo doble-click sobre él. Los módulos pueden estar anidados indefinidamente.

Alias
-----
Los Alias son un tipo de nodo que se utilizan para hacer mas explicativos los diagramas de influencia.
Son un espejo del nodo original. Es decir no solo el resultado que muestran es el mismo sino también que al modificar la definición del alias se modifica la definición del nodo original.
El Alias se crea al apretar **Ctrl+M** una vez seleccionado un nodo. 

----------------------------------------
Operaciones en el Diagrama de Influencia
----------------------------------------

Navegación
----------

El diagrama de influencia es una representación jerárquica de la lógica de cálculo. 
El desplazamiento dentro del diagrama se realiza, haciendo doble-click en el módulo que se quiera entrar o haciendo click en el camino generado a partir de la navegación para subir a las jerarquías superiores.

Inspección de propiedades de nodos
----------------------------------

Al seleccionar un nodo, haciendo click con el botón derecho del mouse, se despliega una ventana de propiedades del nodo.


Arrastrar nodos al diagrama
---------------------------
Haciendo click en el botón azul del extremo superior izquierdo se despliegan los distintos tipos de nodos para arrastrar al diagrama.

.. image:: images/boton_azul.png

Esta es la forma más utilizada de crear nuevos pasos de cálculo en el flujo de procesamiento de datos de la aplicación.

También es posible copiar **<Ctrl+C>**, cortar **<Ctrl+X>** y pegar **<Ctrl+V>** un nodo o grupo de nodos seleccionados.
Para seleccionar varios nodos se debe hacer click sobre cada uno manteniendo la tecla **<Ctrl>** presionada. También se puede generar un rectángulo de selección manteniendo presionada la tecla **<Shift>** y haciendo click sobre el diagrama y luego desplazándose para delimitar el rectángulo.

---------------------------
Visualización de resultados
---------------------------
Al seleccionar un nodo, podemos saber si este está calculado o no, según lo que indica la ventana de resultado:

.. image:: images/not-calc-node.png

Un nodo se calcula al hacer doble-click sobre el mismo o al apretar el icono **Play** que aparece en la ventana de resultado o presionando **<Ctrl+Enter>** una vez seleccionado el nodo.

Existen tres tipos de visualizaciones de un nodo que pueden elegirse en la parte superior derecha de la ventana del diagrama.

.. image:: images/type-of-views.png

* La primera corresponde a la visualización de resultados junto a la documentación.
* La segunda permite ver la definición (código) del nodo junto al resultado del mismo.
* La tercera permite ver el código de la definición del nodo junto a una inspección de las características técnicas del objeto resultante.

