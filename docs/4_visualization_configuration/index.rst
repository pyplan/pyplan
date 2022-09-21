Análisis y Visualización
========================

Uno de los objetivos de Pyplan es proveer transparencia a la lógica de cálculo. Para ello permite no solo navegar por el proceso de calculo para entender conceptualmente su flujo, 
sino también permite evaluar y visualizar los resultados de cada paso.
Esta visualización puede ser en forma de tabla o gráfico, transitoria o permanente.

Pyplan es una plataforma **No-code / Low-code** pensada para usuarios sin conocimientos de programación por lo que permite hacer muchas tareas de manipulación y procesamiento de datos sin necesidad de codificación.

=========================
Manipulación de una Tabla
=========================
Haciendo click sobre el nodo verde con titulo "Data" veremos lo siguiente:

.. image:: images/table_data.png

Maximizando la ventana de visualización (1) y luego haciendo click en (2) accedemos a los datos:

.. image:: images/fed_data.png

Donde podemos ver cada campo y medida de la Tabla, el tipo de campo (Numerico # o Texto T), y la función de agrupamiento que se ejecutará en caso de ser necesario (Suma, Max, Min, Promedio o Conteo)

Arrastrando el campo "Years" a la casilla de columnas y luego de definir el Promedio como función de agregación del campo "atp ranking" lo arrastramos a la casilla de "Medidas" obtendremos una tabla como muestra la siguiente imagen:

.. image:: images/year_rank.png


Esta tabla describe la evolución en el tiempo del ranking promedio anual de "Roger Federer"
Cualquier campo puede ser desplegado como Columna o Fila provocando la agrupación de las medidas visualizadas correspondiente.

.. warning:: Insertar un link a un micro-curso que explique como operar con las tablas

Grafico




* `Dataframe y Series <https://pandas.pydata.org/docs/user_guide/dsintro.html#intro-to-data-structures>`_ de Pandas
* `DataArray <https://docs.xarray.dev/en/stable/user-guide/data-structures.html>`_ de Xarray
* `Array <https://numpy.org/doc/stable/reference/arrays.html>`_ de Numpy



