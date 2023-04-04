Historial de cambios
====================

A continuación se detallan todos los cambios destacables de Pyplan para cada versión:

v3.4.4 - 2023-04-04
-------------------

------------------
Errores corregidos
------------------

- Al abrir app que corre nodos al inicio, se cierra la barra de progreso antes de que termine de correrlos.
- Eliminar escenario no lo quita de los escenarios seleccionados.
- Editor de texto en File Manager no formatea bien archivos .ppm y .ppi.


v3.4.3 - 2023-04-03
-------------------

---------
Novedades
---------

- Integración de PyplanBot con la creación de nodos. Mejora en la experiencia de usuario.
- Nuevo manager para customizar parámetros de PyplanBot y Logs.
- Backup automático cada 1 minuto de assets de una aplicación. Recupero automático cuando desaparece la carpeta assets.
- Nuevo tipo de selector que guarda los labels seleccionados en lugar de las posiciones.
- Wizard de creación de selectores en diagrama.
- Mejora de performance de formularios al confirmar cambios.
- Feedback al apretar botón de Confirmar cambios en un formulario.
- Permitir agregar nuevas columnas a formulario que ya fue creado.
- Crear tabla de usuarios en formularios que contenga su información.
- Opción para que app no intente instalar librerías automáticamente cuando se abre.
- Opción para duplicar componente en una interfaz.
- Configuración inicial para nuevas instalaciones.
- Opción para correr pruebas internas.
- App manager: nuevo botón para importar una app.
- Menú desplegable al hacer click derecho sobre el diagrama.
- Opción para establecer el valor mínimo del eje Y en gráficos.
- Mejora en experiencia de usuario de flechas para encadenar wizards a partir de un nodo.
- Progress bar no bloquea la interfaz. Nuevo parámetro para cerrarla al llegar al 100%.
- Optimizar templates al subir archivos .xls, .xlsx, .xlsm, .xlsb en File Manager.

------------------
Errores corregidos
------------------

- Process manager: validar que si la tarea tiene action type "interface" se mande la interfaz.
- File Manager no se ve en pantalla chica.
- En forms, si pegás más filas de las que tiene el form, da error.
- Al agregar cambios más de una persona en el formulario, a veces se pierden datos.
- Error al cambiar de orden los campos de un formulario.
- Al pegar valores negativos desde Excel en un formulario, se pegan como positivos.
- Al pegar datos desde Excel a un form con selectores relacionados, se sobrecarga la aplicación.
- Setear la versión por defecto debe impactar automáticamente en app.ppl.
- Al crear versión con espacio extra al final, no te deja crear una nueva versión desde ésta.
- Al crear una carpeta en File Manager y en el input presionar delete, aparece el popup de confirmación de borrar.
- Problema al visualizar selectores multiselect en diagrama.
- Al crear un selector no se refresca la definición.
- Si un selector falla, no se puede ingresar al módulo donde se encuentra el selector.
- Al quitarle todos los permisos a un rol, un usuario puede ingresar a funciones que no debería.
- Buscador de nodos de programador de tareas no lista nodos tipo output.
- Ajustes en interfaces.
- Si un usuario falla al loguearse desde más de un navegador distinto, no deja desbloquearlo desde User Manager.
- Buscador de Task Scheduler no funciona correctamente.
- Usuarios con rol Company User no pueden abrir aplicaciones de un Team.
- Al editar un archivo en file manager y dejarlo vacío, no guarda los cambios.


v3.4.2 - 2023-02-04
-------------------

---------
Novedades
---------

- Ahora los nodos pineados de una aplicación persisten entre diferentes sesiones.
- En manager de procesos, los selectores de usuarios ahora muestran nombre y apellido del usuario.

------------------
Errores corregidos
------------------

- Corrección de errores en formularios basados en dataframes cuando se modifica el dataframe origen.
- Al importar un módulo, no lo muestra correctamente en el diagrama.
- No funciona agregar nodos a escenarios haciendo doble click sobre el nodo.
- Error al intentar visualizar un inputnode en una interface dentro de un módulo dennegado.
- Alinear encabezados y botones en managers.


v3.4.1 - 2023-01-27
-------------------

---------
Novedades
---------

- Versionado de aplicaciones.
- Posibilidad de definir, guardar y comparar escenarios.
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


------------------
Errores corregidos
------------------
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
- Otras correcciones menores.


v3.3.6 - 2022-12-12
-------------------

------------------
Errores corregidos
------------------
- Visualización en wizard de creación de indices.
- Corrección de errores al visualizar un dataframe no indexado.
  

v3.3.5 - 2022-12-07
-------------------

------------------
Errores corregidos
------------------
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
 

------------------
Errores corregidos
------------------
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


------------------
Errores corregidos
------------------
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

------------------
Errores corregidos
------------------
- No funciona exportar vista de componente como "Full node".
- En la home y file manager, se pueden ver todos los teams.
- Error al intentar visualizar resultado de objetos no serializables.
- Exportar componente como tabla da error si hay más de una dimensión en columnas.
- Otras correcciones menores.


v3.3.1 - 2022-11-04
-------------------

---------
Novedades
---------

- Ahora las librerías a utilizar en una aplicación se pueden definir en el archivo requirements.txt.
- Permitir configurar colores para cada serie de un gráfico.
- Asistentes que permiten crear el siguiente paso de cálculo.
- Ajustes al confirmar la definición de un nodo.
- Ajustes en la creación de menu.
- El componente menu ahora se puede visualizar por bloques.
- Ajustes en ventanas emergentes.
- Permitir configurar bordes y encabezados en componentes.
- Optimización del uso de librerías.
- Los selectores ahora soportan la opción "Seleccionar todos" para cuando permiten selección múltiple.
- El menú permite agregar subtítulos.


------------------
Errores corregidos
------------------
- Al navegar el diagrama, se resetea el nivel de zoom.
- Error al ejecutar una tarea programada con parámetros.
- Error al editar un campo fecha en un formulario
- En algunas ocasiones al copiar/mover un archivo existente no lo sobre-escribe.
- Los selectores de tipo radio button muestran solo las primeras 10 opciones.
- No muestra el menu principal al abrir desde nueva instancia.
- Error al cerrar instancia desde el Instance Manager.
- Si un dataframe tiene un solo índice, no se puede configurar estilos.
- Al ordenar columna de una tabla está ordenando la columna de totales.
- En algunas ocasiones no se puede editar una tarea programada creada por otro usuario.
- No se visualiza correctamente el breadcrumb cuando se selecciona un Team.
- En formularios, da error al insertar un valor vacío en columna tipo entero o decimal
- Instance manager no funciona correctamente
- Otras correcciones menores.  


v3.2.1 - 2022-07-12
-------------------

---------
Novedades
---------

- Posibilidad de crear campos calculados.
- Reordenar resultado de búsqueda de nodos según criterios.
- Exponer resultado de un nodo como API endpoints.
- Posibilidad de resetear la vista de un componente.

------------------
Errores corregidos
------------------
- Error al hacer drilldowns en tablas.
- Error al cambiar de empresa y volver a file manager.
- Problemas con diálogo de confirmación de cambios no guardados en interfaces
  


v3.1.1 - 2022-06-17
-------------------

---------
Novedades
---------

- Nueva y moderna interface de usuario.
- Nuevo concepto de aplicaciones (integrando lógica, interfaces y formularios).
- Se agregaron nuevos componentes de tipo gráfico (incluye todos los gráficos de la librería plotly).
- Interface de usuario para la creación de formularios.
- Posibilidad de personalizar el código de cada componente de una interface.
- Nuevo diagrama de influencia (estandarización de colores de nodos).
- 3 vistas de código.
- Ayudas en codificación.
- Wizards para la creación de nodos.
- Consola de output y errores.
- Mejora general en la performance.