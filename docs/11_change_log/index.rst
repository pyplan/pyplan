Historial de cambios
====================

A continuación se detallan todos los cambios destacables de Pyplan para cada versión:


v3.4.1 - 2023-01-27
-------------------

---------
Novedades
---------

- Versionado de aplicaciones.
- Posibilidad de definir, crear y comparar escenarios.
- Manager de procesos (workflow).
- Nueva vista "Mis tareas".
- Nuevo diseño de la página de inicio.
- Permitir agregar imágenes en miniatura (thumbnail.png) para aplicaciones.
- Editor de texto dentro del administrador de archivos.
- Más opciones de formato condicional.
- Nuevas funciones pp.download() y pp.upload().
- Exportar/importar interfaces.
- Mejora en las respuestas de pyplan-bot.
- Mejora en la documentación de las funciones pp.


---------------------
Corrección de errores
---------------------
- Error al crear carpetas con espacio al final del texto.
- Paginación en selectores.
- Error al pegar números formateados desde Excel.
- Error al cancelar cambios en form que no fue confirmado.
- Al editar el nombre de una carpeta o archivo y presionar delete, intenta eliminar el archivo.
- Al completar default value de una columna de un form y luego borrarlo, da error el generar definición
- Problemas de scroll en área de pivoteo de tablas y gráficos.
- Error al navegar el diagrama si la definición de un nodo tipo input tiene un error.
- No funcionan los selectores relacionados del form basado en un dataframe.
- En menú tipo bloques, no deshabilita bloques para los cuales el usuario no tiene permisos.
- No funciona copiar y pegar / duplicar módulos.
- No funciona links a dashboards cuando en una interface existe mas de un link.


v3.3.6 - 2022-12-12
-------------------

---------------------
Corrección de errores
---------------------
- Visualización en wizard de creación de indices.
- Corrección de errores al visualizar un dataframe no indexado.
  

v3.3.5 - 2022-12-07
-------------------

---------------------
Corrección de errores
---------------------
- Error al insertar un valor en un input table.


v3.3.4 - 2022-12-07
-------------------

---------
Novedades
---------
- Nuevo pyplan-bot (OpenAI-GPT3)
- Nueva función pp.progressbar()
- Wizard para realizar cambio de indice.
- Ejemplo de aplicaciones en home.
 

---------------------
Corrección de errores
---------------------
- Scroll en Filemanager.
- Error al arrastrar componente tipo chart.



v3.3.3 - 2022-12-02
-------------------

---------
Novedades
---------
- Nuevas variantes de colores de heatmap para tablas.
- Ajustes en pestaña de Performance.
- Permitir cambiar el idioma de Pyplan.


---------------------
Corrección de errores
---------------------
- Al cambiar tipo de visualización (tabla -> gráfico -> tabla), no aplica código personalizado.
- Error en estilos de radio buttons.


v3.3.2 - 2022-11-29
-------------------

---------
Novedades
---------

- Asistente de conversión de datarray a dataframe.
- Asistente de creación de indices.
- Aplicar formato a ejes y hover en charts.
- Unificar componentes inputs.
- Agregar documentación a interfaces.
- Nueva funcionalidad análisis de performance.
- Cambios en jerarquías de índices.
- Uso de la carpeta Media para almacenar imágenes, documentos, etc.

---------------------
Corrección de errores
---------------------
- No funciona exportar vista de componente como "Full node".
- En la home y file manager, se pueden ver todos los teams.
- Error al intentar visualizar resultado de objetos no serializables.
- Exportar componente como tabla da error si hay más de una dimensión en columnas.


v3.3.1 - 2022-11-04
-------------------


v3.2.1 - 2022-07-12
-------------------


v3.1.1 - 2022-06-17
-------------------
