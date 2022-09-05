Análisis y Visualización
========================

Uno de los objetivos de Pyplan es proveer transparencia a la lógica de cálculo. Para ello permite no solo navegar por el proceso de calculo sino también la posibilidad de evaluar y visualizar los resultados de cada paso.
Esta visualización puede ser en forma de tabla o gráfico, transitoria o permanente.

El modelo de calculo 

Para entender como configurar la visualización de un nodo es necesario entender primero los tipos de objetos que Pyplan interpreta de forma nativa.
Estos son:

* `Dataframe y Series <https://pandas.pydata.org/docs/user_guide/dsintro.html#intro-to-data-structures>`_ de Pandas
* `DataArray <https://docs.xarray.dev/en/stable/user-guide/data-structures.html>`_ de Xarray
* `Array <https://numpy.org/doc/stable/reference/arrays.html>`_ de Numpy

En pocas palabras un Dataframe es una estructura del tipo tabla donde cada columna corresponde a un atributo o medida. Cada fila corresponde a un registro particular de esos atributos o medidas.


=========================
Objetos nativos de Pyplan
=========================

