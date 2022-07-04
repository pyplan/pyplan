# ![Pyplan](./docs/images/logo.png)

Repositorio para la documentación de Pyplan

## Requerimientos

* [python 3](https://www.python.org/downloads/)

## Clonar el repositorio

``` bash
cd  [tu-path-de-proyectos]
git clone https://github.com/pyplan/pyplan.git
```

## Configurar el entorno

``` bash
# Create virtual environment
cd [tu-path-de-proyectos]/pyplan
python3 -m venv venv
. venv/bin/activate # in linux/mac os
venv\Scripts\activate.bat # in windows
pip install --upgrade pip
pip install -r requirements.txt
```

## Live preview

``` bash
cd [tu-path-de-proyectos]/pyplan
# For Spanish
sphinx-autobuild docs docs/_build/html/es -D=language=es --port 5500 --open-browser
# For English
sphinx-autobuild docs docs/_build/html/en -D=language=en --port 5500 --open-browser
```


## Como contribuir

1. Actualizar la rama  local **main**.
2. Crear una nueva rama con un nombre descriptivo (Ej. schedule-task), desde la rama **main**.
3. Modificar/crear archivos de documentación .rst/.md, dentro de la carpeta **/docs**. Tener en cuenta la estructura que se muestra en el punto siguiente.
4. Al terminar, realizar un Pull Request desde la nueva rama hacia la rama **main**.

## Estructura de archivos
La documentación se puede escribir en archivos de formato .rst (reStructuredText) o .md (markdown). Preferentemente se utilizará el formato rst. [Cheat Sheet](https://docs.typo3.org/m/typo3/docs-how-to-document/main/en-us/WritingReST/CheatSheet.html) Todos los archivos de documentación se ubican dentro de la carpeta **/docs**. Se deberán organizar los temas por subcarpetas. Ejemplo: **/docs/user_guide/**. Para agregar imágenes, crear una carpeta **images** en el mismo path donde se encuentra el archivo .rst que utiliza dicha imagen.


## Generar archivos de traducción (para uso interno)

``` bash
cd [tu-path-de-proyectos]/pyplan/docs
# create/update POT files
make gettext
# create/update PO files for translations
sphinx-intl update -p _build/gettext -l en
```
