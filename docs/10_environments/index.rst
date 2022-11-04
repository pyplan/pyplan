Entornos virtuales
==================

Los entornos virtuales son repositorios donde se instalan las librerías de python que utiliza una aplicación.
Pyplan gestiona estos entornos virtuales de manera automática, recargándonos al momento de abrir una aplicación.


Funcionamiento
--------------

Al momento de abrir una aplicación desde el espacio Público, se pre-carga el entorno de dicha aplicación que reside en el espacio Público.

Si un usuario abre la aplicación desde su propio espacio de trabajo, y en su espacio de trabajo no existe el entorno de dicha aplicación, 
se pre-cargará el entorno del espacio público. En este caso, si el usuario necesita realizar cambios en las librerías, se mostrará el siguiente mensaje:


# TODO: imagen 

Al hacer click en el botón "yesxxxxx", se creará y se cargará el entorno de manera local, o sea en el espacio del usuario. Esto permitirá 
realizar cambios ya sea instalando librerías o modificando el archivo requirements.txt


Instalar librerías
------------------

Puede instalar librerías de python utilizando la pestaña "install" y escribiendo el nombre de la librería a instalar, o bien en la solapa 
"requirements" puede modificar de manera manual el archivo requirements.txt.


Identificación de aplicación
----------------------------

Cada aplicación de Pyplan posee un identificador único que se puede visualizar ingresando a la opción de propiedades de la aplicación. 


# TODO: image

Este identificador se genera al crear una nueva aplicación y es utilizado para identificar el entorno virtual asociado a la aplicación. Por lo tanto 
cada aplicación podrá tener su propio set de librerías.

#Tip, si desea crear una aplicación nueva partiendo de otra, utiliza la función "crear desde". De esta manera te aseguras de que se genere
un nuevo identificador para la aplicación que se está or crear.


Utilizando entornos por primera vez
-----------------------------------

Si está por abrir una aplicación que se creó con una versión anterior a Pyplan 3.3.1, en el proceso de apertura se creará el entorno virtual 
de dicha aplicación. Este proceso puede llevar bastante tiempo, dependiendo de las librerías usadas por la aplicación. 

Puede ver el avance de la instalación de librerías haciendo click aquí:

#TODO image
