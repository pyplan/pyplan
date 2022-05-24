# ![Pyplan](./docs/assets/logo.png)

Repository for documentation of Pyplan

## Requirements

* [python 3](https://www.python.org/downloads/)

## Clone the repository

``` bash
cd  [your-project-path]
git clone https://github.com/pyplan/pyplan.git
```

## Prepare for build

``` bash
# Create virtual environment
cd [your-project-path]/pyplan
python3 -m venv venv
. venv/bin/activate # in linux/mac os
venv\Scripts\activate.bat # in windows
pip install --upgrade pip
pip install -r requirements.txt
```

## Live preview

``` bash
cd [your-project-path]/pyplan
sphinx-autobuild -a docs docs/_build/html --port 5500 --open-browser
```

## Contribute

TODO: describir bien el proceso

1. Actualizar la rama sobre la cual se quiere documentar
2. Crearuna rama nueva, partiendo de la rama base
3. Modificar/crear archivos .rst de documentacion dentro de la carpeta /docs
4. Realizar un Pull request seleccionando como origen la nueva rama y destino la rama que se quiere actualizar

## Build

``` bash
cd [your-project-path]/pyplan/docs
make html
```