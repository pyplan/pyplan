Historial de cambios
====================

A continuación se detallan todos los cambios destacables de Pyplan para cada versión:

v3.7.2 - 2023-12-12
-------------------

------------------
Errores corregidos
------------------

- Correcciones mínimas.


v3.7.1 - 2023-12-11
-------------------

---------
Novedades
---------

- Al abrir una interfaz, mostrar recursos cada dos segundos.

------------------
Errores corregidos
------------------

- Error al guardar aplicación con selector que tiene parámetros no serializables.


v3.7.0 - 2023-12-07
-------------------

---------
Novedades
---------

- Nuevo add-in para Microsoft Excel de Pyplan.
- Nuevo sistema de notificaciones de una aplicación.
- Nuevas opciones para personalizar la invalidación de outputs o la confirmación de cambios en formularios.
- Agregar opciones de copiar aplicación al Public y a un Team desde Administrador de aplicaciones.
- Nuevo formato de visualización de componente Selector de forma que se vea como chips elegibles clickeables.
- Nuevo formato de visualización de componente Index de forma que se vea como un selector.
- Nuevo parámetro en tareas programadas para seleccionar usuarios a los que se les enviará un email al finalizar la tarea.
- Permitir aplicar acciones como eliminar o archivar a múltiples versiones al mismo tiempo.
- Permitir aplicar acciones como eliminar a múltiples escenarios al mismo tiempo.
- Se agregó el rol del usuario en la vista de información de su cuenta.
- Autochequear checkbox de Borrar/recrear tabla en formularios ante cambios estructurales al editarlo.
- Permitir fijar nodos de tipo módulo para navegar rápidamente a ellos.
- En escenarios, guardar selectores e input scalars que son inputs de los nodos a guardar.
- En componente HTML, si un link a interfaz tiene target='_self', al hacerle click, abrir interfaz y cerrar tab actual.

------------------
Errores corregidos
------------------

- No se puede crear una nueva versión en un Team si el usuario no tiene permisos para ver todas las carpetas de la compañía.
- Al desincronizar índices de un componente, no funciona aplicar filtros a ese mismo componente.
- Si definición con dynamic tiene caracter "\", dynamic no funciona.
- Al buscar en selector de formularios, los resultados se reordenan de forma arbitraria.
- Agregar loader a componente tipo Index cuando se están cargando los valores.
- Al recargar aplicación con cambios pendientes no guardados, no limpia el estado de cambios pendientes sin guardar.
- En diagrama, al dibujar selector debería llegar los datos con el último valor guardado para no ejecutar su result.
- Si una tarea de un proceso pasa de estado "Completada" a "No iniciada", borrar fecha de finalización.
- Al crear un alias, seleccionar el nuevo nodo alias.
- Input Scalar con valor no serializable rompe UI.
- En algunas resoluciones la ventana de login no se ve correctamente.
- Al agregar mapa de jerarquías a un nodo en el diagrama, no muestra el ícono de jerarquía en el nodo hasta que no se refresca el diagrama.
- Si borrás un componente de una interfaz con un sólo componente, no te lo deja borrar.
- Al cerrar sesión en una pestaña, redireccionar las otras pestañas abiertas a la pantalla de login.
- Correcciones mínimas.


v3.6.16 - 2023-11-09
--------------------

---------
Novedades
---------

- Agregar posibilidad de guardar cambios pendientes de aplicación en una nueva versión.
- Agregar loader al navegar Administrador de archivos.

------------------
Errores corregidos
------------------

- Duplicar procesos arroja error en algunas ocasiones.
- Exportar componente con múltiples dimensiones en columnas arroja error.
- Correcciones mínimas.


v3.6.15 - 2023-11-05
--------------------

---------
Novedades
---------

- Al cambiar jerarquía desde componente Index, que automáticamente actualice el resto de componentes donde ese índice esté a la jerarquía elegida.
- Al crear versión, si el usuario no tiene permisos de escritura en el directorio, guardar aplicación y nueva versión en su espacio privado.
- Agregar loader al cambiar de compañía.
- Cambiar texto de medida de agregación "Media" por "Promedio".

------------------
Errores corregidos
------------------

- Al consolidar un módulo que no existe en la aplicación de destino, siempre lo agrega en el root del diagrama.
- Al consolidar una aplicación, las interfaces muestran resultados anteriores a la consolidación.
- Al renombrar una versión que es la versión por defecto de la aplicación, no la renombra en el archivo app.ppl.
- No se ve todo el diálogo de lectura de Excel en resoluciones bajas.
- En ciertas ocasiones no se actualiza correctamente la aplicación o la versión en la barra superior.
- Al cerrar una de varias instancias abiertas en la Home de Pyplan, siempre cierra la última.
- Quedan instancias abiertas cuando no están disponibles.
- Correcciones mínimas.


v3.6.14 - 2023-10-29
--------------------

------------------
Errores corregidos
------------------

- No funciona crear nodo desde PyplanBot.


v3.6.13 - 2023-10-27
--------------------

---------
Novedades
---------

- Al activar escenarios en tablas, colocar dimensión Pyplan Scenarios en las columnas en lugar de las filas.

------------------
Errores corregidos
------------------

- Ancho de encabezado de componentes en código personalizado se ve cortado cuando tiene color de fondo.
- No funciona botón de aplicar wizards en widget de código.


v3.6.12 - 2023-10-26
--------------------

---------
Novedades
---------

- Nueva funcionalidad para aplicar paletas de colores personalizadas a gráficos.
- Cambio en color por defecto de componentes de tipo Tabla y Gráfico.

------------------
Errores corregidos
------------------

- No activar checkbox de Borrar y recrear tabla automáticamente al agregar o eliminar una columna de un formulario.
- Ancho de encabezado de componentes en diagrama se ve cortado cuando tiene color de fondo.
- Actualizar año de copyright en sección de Acerca de.
- Correciones mínimas.


v3.6.11 - 2023-10-25
--------------------

------------------
Errores corregidos
------------------

- Correciones mínimas.


v3.6.10 - 2023-10-25
--------------------

---------
Novedades
---------

- Agregar ícono para filtrar en etiquetas de columnas en tablas planas.
- Crear administrador de plantillas de escenarios.
- Permitir seleccionar múltiples nodos al elegir nodos para una plantilla de escenarios.
- Agregar lista de nodos a evaluar antes de guardar un escenario a plantillas de escenarios.
- Agregar ícono en componente para activar/desactivar la comparación de escenarios.
- Otras mejoras en escenarios.
- Permitir aplicar formato numérico a componente InputValue.
- Mejoras en gráficos Waterfall y Combinado.
- Al ingresar a un módulo, agregar loader mientras carga el módulo.
- Cambio en color de fondo de celdas no editables en modo claro.
- Agregar ícono para cambiar jerarquía de un componente tipo Índice que tiene jerarquías establecidas.
- Ocultar botón de maximizar componente en componentes que no sean de tipo Tabla o Gráfico.
- Mover ícono de maximizar a la derecha del título del componente.
- Agregar ícono para seleccionar jerarquías de forma rápida en componentes de tipo Tabla y Gráfico.
- Agregar propiedad de componente para personalizar color de texto y fondo de título de un componente.
- Adecuar font-family de gráficos de Plotly al resto de Pyplan.
- Habilitar por defecto la opción de permitir agregar nuevas columnas en la creación de nuevos formularios.
- Agregar departments a usuarios en función pp.get_user_list.
- Nueva función pp.get_all_processes para obtener el listado de todos los procesos y sus tareas que contiene la aplicación abierta.
- Nuevas funciones pp.where, pp.maximum y pp.minimum.

------------------
Errores corregidos
------------------

- Si el resultado de un nodo es de tipo Generic y el resultado es un string de tamaño considerable, se rompe el explorador.
- Tabla de pestaña de Performance en consola no muestra bien los porcentajes.
- Guardar ID de nodo original al guardar los nodos afectados a un escenario.
- Menú contextual de wizards en un nodo se mueve a la esquina superior izquierda por error.
- Si existe un componente con escenarios como dimensión y luego se quitan todos los escenarios cargados, se rompe la visualización.
- Correciones mínimas.


v3.6.9 - 2023-09-28
--------------------

---------
Novedades
---------

- Agregar funcionalidad de aplicar columnas jerárquicas a formularios.

------------------
Errores corregidos
------------------

- Error al consolidar interfaces que no tienen propiedad "definition".


v3.6.8 - 2023-09-27
--------------------

---------
Novedades
---------

- Agregar permiso para mostrar botón que oculta archivos en Administrador de archivos.


v3.6.7 - 2023-09-26
--------------------

---------
Novedades
---------

- Reorganización de opciones de menú lateral.
- Ajustes en Consolidación de aplicaciones.
- Agregar posibilidad de mostrar un diálogo de confirmación al apretar un botón en una interfaz.

------------------
Errores corregidos
------------------

- Si hay progress bar y modal de nodo corriendo simultáneamente, sólo muestra progress bar. Debe mostrar ambos.
- Selector de nodos de Administrador de tareas no funciona correctamente.
- Correcciones mínimas.


v3.6.6 - 2023-09-19
--------------------

------------------
Errores corregidos
------------------

- Correcciones mínimas.


v3.6.5 - 2023-09-18
--------------------

------------------
Errores corregidos
------------------

- No es posible confirmar definición en nodos de tipo Botón.
- Al consolidar nodos con cambios en la propiedad nodeInfo, arroja error al confirmar.
- Selectores no permiten elegir valores si existe alguna opción con caracteres "(" o ")" en su dominio de valores posibles.


v3.6.4 - 2023-09-15
--------------------

---------
Novedades
---------

- Permitir renombrar, activar y cerrar versión abierta.
- Agregar propiedad en componentes para ocultar/mostrar ícono de manipulación de datos.
- Al seleccionar opción "All" en selectores múltiples, guardar array vacío en definición que indique que todas las opciones están seleccionadas.
- Cambiar color de fondo y texto por defecto de celdas de valores en tablas.
- Validar contraseña actual al cambiar la contraseña del usuario actual.
- Modificar componente HTML para que detecte links a interfaces con xlink:href.
- Permitir copiar URL al seleccionar un archivo dentro de la carpeta Media en Administrador de archivos.
- Mostrar número de versión según tag de imágenes utilizadas.

------------------
Errores corregidos
------------------

- Exportar tabla a Excel como "Full node" demora mucho tiempo y utiliza mucha memoria.
- No funciona acción de desplazar diagrama en dispositivos táctiles.
- Validar en formularios que todos las columnas tengan un field no vacío antes de crear la tabla en la base de datos.
- Nodo seleccionado se marca con cambios pendientes de confirmación aún no habiendo hecho cambios.
- Luego de apretar botón de refresh en una interfaz, al hacer un cambio en un índice y cambiar a otra interfaz, al volver a la interfaz original te mantiene el cambio.
- Si una columna de un dataframe que alimenta un formulario es de tipo float32, el formulario se rompe.
- Problemas de posicionamiento al hacer click en opción de "Ir al nodo" de un componente de interfaz.
- Al recargar Pyplan con una instancia vencida, en ocasiones recupera la instancia de otro usuario.
- Correcciones mínimas.


v3.6.3 - 2023-09-07
--------------------

---------
Novedades
---------

- Agregar opciones con click derecho en tablas para copiar incluyendo los encabezados.
- Agregar propiedad de aplicación para elegir qué pestaña elegir entre "Seleccionar versión existente" o "Crear nueva versión".
- Mejoras en búsqueda en Administrador de archivos.
- Si se abre una nuevo pestaña del explorador en una sección que necesita una instancia, si existe una recuperarla.
- Aceptar distintos formatos de fecha para pegar en formularios con campo de tipo fecha.
- Agregar opción en componentes de interfaces para no mostrar ícono de maximizar.
- En menú de interfaces, agregar nuevas rutas de Pyplan para navegar dentro de la aplicación.
- Agregar posibilidad de anular contraseña en interfaces externas.

------------------
Errores corregidos
------------------

- Impedir evaluación concurrente de nodos.
- No es posible eliminar el estilo autogenerado de formularios para las columnas numéricas.
- Índice en formato Oculto no resetea a los valores guardados al refrescar la interfaz.
- No se ordenan correctamente las filas del Administrador de instancias.
- Filtrar listado de tareas de workflow en base a la compañía actual.
- En algunas aplicaciones no deja confirmar cambios en propiedades de la aplicación.
- Si no se carga un usuario que corra una tarea programada, arroja error.
- En Administrador de logs, no muestra nada en campo "Model".
- No se ve link de resetear password en email de recuperar contraseña en modo claro.
- Correcciones mínimas.


v3.6.2 - 2023-08-30
--------------------

---------
Novedades
---------

- Mejora en performance al obtener flechas en diagrama.


v3.6.1 - 2023-08-28
--------------------

------------------
Errores corregidos
------------------

- Se reporta alto uso de CPU constantemente con cgroup v1.


v3.6.0 - 2023-08-25
--------------------

---------
Novedades
---------

- Nueva sección para consolidar módulos, interfaces y archivos entre dos versiones de una aplicación.
- Tareas programadas pueden agregarse como widget en una interfaz.
- Mejora en workflow: nuevo estado "Not ready to start" dependiente de que tareas bloqueantes finalicen antes de permitir avanzar en el proceso.
- Mejora en workflow: nuevo tipo de expiración de tarea "desde que se completó la tarea bloqueante".
- Mejora en workflow: nuevo campo "Interfaz de revisión" para asignar una interfaz al usuario revisor.
- Mejora en workflow: sólo mostrar tareas en las que el usuario es responsable, revisor o subscriptor. En caso de ser subscriptor del proceso, mostrar todas.
- Mejora en workflow: no permitir que el usuario elegido como responsable de la tarea pueda ser elegido como revisor o subscriptor de la misma.
- Nuevas funciones PyplanFunctions para consumir/interactuar con workflow con código desde la aplicación: pp.get_my_processes, pp.get_task_statuses y pp.change_task_status.
- Funcionalidad para elegir qué columnas visualizar en widget de tareas de workflow.
- Nuevo rol estándar "Creator with Public Access".
- Permitir ordenar por cualquier columna en Administrador de Instancias.
- Al ingresar vía SAML, siempre permitir elegir la compañía si el usuario está asignado a más de una.
- Agregar campos "Creation Date", "Last Password Change", "MFA Enabled" y "Deleted" a reporte de usuarios que se exporta desde Administrador de Usuarios.

------------------
Errores corregidos
------------------

- Al seleccionar un nodo y luego un texto, no es posible volver a seleccionar el nodo original.
- No funciona la obtención de recursos utilizados con cgroup v2.
- No se visualizan correctamente los resultados de tipo str, dict o list o bool en interfaces.
- En interfaces externas no se muestra el ícono para deplegar el menú de interfaces.
- Corrección en workflow: al cambiar el estado de una tarea desde Completado a otro estado anterior (reversión), las tareas que dependen de ella deben bloquearse nuevamente.
- Si un nodo contiene texto en formato HTML, al arrastrarlo a una interfaz no funciona el "Go to node".
- En Permisos por rol, al apretar en checkbox de "All" de una sección, aplica a todas las secciones.
- Al crear/editar un proceso, al intentar crear un grupo de tareas teniendo un grupo seleccionado de la tabla, edita el grupo seleccionado.
- Al solicitar cambiar contraseña en login, si se quita el "/auth/"" de la URL, es posible continuar sin cambiar la contraseña.
- Correcciones mínimas.


v3.5.6 - 2023-07-28
--------------------

------------------
Errores corregidos
------------------

- Componente Dash no refresca al cambiar un input en un nodo relacionado.
- Correcciones mínimas.


v3.5.5 - 2023-07-27
--------------------

---------
Novedades
---------

- Nuevos roles por defecto: Administrator, App Administrator, Creator, Explorer, Viewer. Usuarios con rol Pyplan Admin asumen rol de Administrator. Usuarios Company Admin, App Administrator. Usuarios Company User, Creator.
- Tareas de workflow pueden agregarse como widget en una interfaz. Desaparece vista de Mis tareas.
- Mejoras estéticas en tabla de Mis tareas de workflow y al agregar un tareas en un proceso.
- Validar que correo electrónico sea único al agregar nuevos usuarios.

------------------
Errores corregidos
------------------

- Visualización de formulario se rompe al aplicar más de un filtro.
- No es posible borrar una carpeta con espacios al final.
- No permitir ajustar tamaño ni mover componente maximizado en una interfaz.
- No funciona buscador de tareas programadas.
- Etiqueta de botones no se ven bien al aumentar el tamaño de fuente.
- Correcciones mínimas.


v3.5.4 - 2023-07-14
--------------------

---------
Novedades
---------

- Funcionalidad para abrir una app al iniciar sesión configurable por departamento.
- Guardar última carpeta abierta en Interface Manager al navegar interfaces.
- Nueva función pp.get_user_list() permite obtener listado de usuarios de la compañía.
- Autenticación de múltiples factores por código de única vez enviado a e-mail.
- Funcionalidad para personalizar estilos de botones en interfaces.
- No ordenar ni filtrar filas no confirmadas en formularios.

------------------
Errores corregidos
------------------

- Al recibir mensajes en PyplanBot, no es posible hacer scroll hacia arriba.
- Si el resultado de un nodo es de tipo string, no es posible configurarle estilos personalizados.
- Al finalizar wizard de Transformar desde un dataframe a un índice, no se visualiza el nodo en el diagrama.
- No es posible cambiar tamaño de nodo tipo texto si está dentro de otro nodo tipo texto.
- Correcciones mínimas.


v3.5.3 - 2023-07-07
--------------------

------------------
Errores corregidos
------------------

- No es posible visualizar nodos con un string con código HTML.
- Login con SAML pide cambiar contraseña vencida.
- Correcciones mínimas.


v3.5.2 - 2023-07-06
--------------------

------------------
Errores corregidos
------------------

- Copiar y pegar valores de tabla pega títulos de columnas.
- Correcciones mínimas.


v3.5.1 - 2023-07-06
--------------------

---------
Novedades
---------

- Funcionalidad para compartir interfaces con usuarios externos de Pyplan.
- Autenticación con múltiples factores en login de usuarios (MFA).
- PyplanBot responde consultas sobre Pyplan.
- Asistente de Bot por compañía como widget de interfaces.
- Wizard para comparar dos o más nodos.
- Mostrar tareas programadas de sistema en Task Manager.
- Crear rol "Login Only User" que sólo tenga permisos para loguearse para todas las compañías.

------------------
Errores corregidos
------------------

- Copiar tabla a una planilla Excel no pega títulos de columnas.
- Visualización de algunos tipos de nodos no se actualizan al cambiar definición y evaluar nuevamente.
- En algunas ocasiones, al hacer ALT + Click en un nodo desde el widget de código trae el id del nodo sin el último caracter.
- Selector de formato Radio buttons en orientación vertical no muestra opción "All" si es multiselect.
- Si el resultado de un nodo es un string, no es posible configurarle estilos como si fuera un Indicator.
- En interfaces, no deja importar alias de Index al elegir tipo de componente Index.
- Correcciones mínimas.


v3.4.17 - 2023-06-15
--------------------

------------------
Errores corregidos
------------------

- Al crear visualización de componente por primera vez, sólo elegir formato numérico si el tipo de dato de las medidas es numérico.
- Al visualizar una celda con un valor con formato de fecha, lo transforma a número.


v3.4.16 - 2023-06-14
--------------------

---------
Novedades
---------

- Elementos calculados para una dimensión en tablas y gráficos.
- Autenticación con API key para links externos.
- Posibilidad de setear permisos a más de una interface al mismo tiempo.
- Visualización nativa de gráficos de Matplotlib.

------------------
Errores corregidos
------------------

- No funciona el formato condicional aplicado a columnas de tipo selector en formularios.
- No funcionan opciones de formato condicional en indicadores.
- Si tabla tiene mezcla de números y texto como valores, no funciona formato numérico.
- Al hacer click en opción "Go to node", centrar diagrama en nodo elegido.
- Al estar editando una interface, si se elige "Go to node" en un componente, nunca te redirige al nodo.
- Componente Índice en interfaces no se ve bien cuando sus valores son booleanos (True, False).
- Al crear nuevas interfaces, no aparecen en listado de interfaces del editor del Menú hasta que se recarga la aplicación.
- No funciona paginación en Administrador de logs.
- Al abrir un módulo que contiene un nodo de tipo InputScalar con error, no abre el módulo.
- Home de Pyplan da error si existe más de un Team con el mismo nombre.
- Error en código generado por wizard de Seleccionar filas.
- Tabla plana no muestra títulos de índices cuando el identifier de un índice coincide con el nombre de la columna.
- Selector de condiciones de estilos no trae columnas cuando la tabla es plana.
- Mejoras en Administrador de instancias.
- Correcciones mínimas.


v3.4.15 - 2023-05-23
--------------------

------------------
Errores corregidos
------------------

- Correcciones mínimas.

v3.4.14 - 2023-05-22
--------------------

---------
Novedades
---------

- Filtrar resultados al buscar texto en selector de formularios.

------------------
Errores corregidos
------------------

- Al pegar más de una fila que contiene fechas en un form, no se pegan todas las filas.
- Al ingresar un valor en un Input variante Cubo o Tabla (InputDataArray o InputDataFrame), se refresca y el foco vuelve al inicio.
- Correcciones mínimas.

v3.4.13 - 2023-05-19
--------------------

---------
Novedades
---------

- Funcionalidad para cambiar colores a series de gráfico tipo Combinado.
- Funcionalidad para exportar chat con PyplanBot.
- Permitir elegir con qué usuario ejecutar una tarea programada.
- Funcionalidad para formatear código en widget de código de diagrama.

------------------
Errores corregidos
------------------

- Al crear un nodo tipo Input variante Cubo (InputDataArray), no se puede asignar como valor por defecto un nodo cuyo resultado sea np.nan.
- Celda con selector en formularios se "corta" cuando llega hasta el final de la tabla.
- No es posible copiar id de nodo con ALT + Click si está seleccionado el widget de Resultado en diagrama.
- Error al ordenar por roles a usuarios en User Manager.
- En campos calculados de una tabla, el valor de los totales no se está calculando.
- Evitar cambiar automáticamente las vistas del diagrama al cambiar de elemento seleccionado.
- Correcciones mínimas.


v3.4.12 - 2023-05-15
--------------------

------------------
Errores corregidos
------------------

- Correcciones mínimas.


v3.4.11 - 2023-05-13
--------------------

------------------
Errores corregidos
------------------

- Correcciones mínimas.


v3.4.10 - 2023-05-12
--------------------

---------
Novedades
---------

- Al abrir aplicación, permitir elegir versión en lugar de abrir la versión por defecto (propiedad nueva; por defecto, desactivada).
- Interacción de componentes de Dash con componentes nativos de la app.
- Comparación de escenarios no ejecuta escenario Current si no fue elegido para compararse.
- Permitir filtros en interfaces si el título del nodo de un índice coincide con el nombre de la dimensión/columna en otro componente.
- Agregar nuevo permiso de si se permite "Guardar como" una aplicación.
- Mejorar estética de componente Menú formato "Cajas".
- Vencimiento de contraseñas por empresa.
- Funcionalidad "Olvidé mi contraseña".
- Funcionalidad para forzar cambiar contraseña al crear un nuevo usuario.
- Nuevas imágenes en página de login.
- Envío de mensaje cuando la licencia de Pyplan en la compañía está próxima a su vencimiento.
- Funcionalidad para repreguntar en PyplanBot.
- Funcionalidad para detener respuesta de PyplanBot.
- Ícono con declaración de privacidad en PyplanBot.

------------------
Errores corregidos
------------------

- Editar un valor de una columna tipo integer de un formulario arroja un error.
- Formato condicional en tabla no inserta ícono si celda no es de tipo numérica.
- En ocasiones, la ventana emergente del intellisense del código no se alcanza a ver por completo.
- Ciertos grupos de permisos están duplicados en Permisos por rol.
- Al recargar aplicación, abre siempre la versión por defecto a pesar de tener abierta otra versión.
- Correcciones mínimas.


v3.4.9 - 2023-04-24
-------------------

------------------
Errores corregidos
------------------

- En una columna tipo selector con valores relacionados en un formulario, sólo es posible elegir entre las primeras 100 opciones.
- Al instalar librerías, si la instalación falla, igualmente agrega la librería al archivo requirements.txt.


v3.4.8 - 2023-04-21
-------------------

---------
Novedades
---------

- Agregar ícono para guardar vista por defecto en widget de resultado en diagrama.
- Funcionalidad para copiar, cortar y pegar en Interface Manager.
- Al crear una interfaz, abrirla en modo edición.
- Al archivar una versión, la carpeta se comprime en un archivo .zip.
- Agregar campo de descripción a versiones.
- Funcionalidad para abrir archivos (.txt, .json, .ppm, .ppi) y descomprimir archivos (.zip) al hacer doble click en File Manager.
- Nuevo manager de links externos generados (API endpoints de nodos).
- Mejoras en feedback al subir archivos.
- Mejoras en la experiencia de usuario de PyplanBot.

------------------
Errores corregidos
------------------

- Al hacer click en un nodo con documentación, en ocasiones no la muestra.
- Maximizar widget de resultado no debe superponerse a barra de nodos anclados.
- Al crear un alias de un nodo, queda seleccionado el alias y no el nodo original.
- Exportación como "Full node" no funciona correctamente.
- Al importar una interfaz, si ya existe una interfaz con mismo nombre, la nueva debe conservar el id y la vieja cambiar su id y nombre.
- No es posible navegar carpetas en Interface Manager si la versión de la app contiene caracteres especiales como "+".
- Al abrir una app con una instancia preexistente abierta, no carga las interfaces al abrir.
- Al moverse con flechas de teclado en widget de resultado o código, se mueve también el nodo en el diagrama.


v3.4.7 - 2023-04-14
-------------------

------------------
Errores corregidos
------------------

- Correcciones mínimas.


v3.4.6 - 2023-04-13
-------------------

------------------
Errores corregidos
------------------

- Al abrir, recargar o cambiar versión de aplicación, en ocasiones no carga la aplicación.


v3.4.5 - 2023-04-11
-------------------

---------
Novedades
---------

- Mejoras en la experiencia de usuario de PyplanBot.

------------------
Errores corregidos
------------------

- Logs manager no funciona.
- Editor de menú no vincula correctamente las interfaces asociadas a acciones cuando existen más de 50 interfaces.
- Correcciones varias.


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
- Al completar default value de una columna de un form y luego borrarlo, da error el generar definición.
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
- En formularios, da error al insertar un valor vacío en columna tipo entero o decimal.
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