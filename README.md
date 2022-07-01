# ![Pyplan](./docs/images/logo.png)

Repository for documentation of Pyplan

## Requirements

* [python 3](https://www.python.org/downloads/)

## Clone the repository

``` bash
cd  [your-projects-path]
git clone https://github.com/pyplan/pyplan.git
```

## Configure environment

``` bash
# Create virtual environment
cd [your-projects-path]/pyplan
python3 -m venv venv
. venv/bin/activate # in linux/mac os
venv\Scripts\activate.bat # in windows
pip install --upgrade pip
pip install -r requirements.txt
```

## Live preview

``` bash
cd [your-projects-path]/pyplan
# For Spanish
sphinx-autobuild docs docs/_build/html/es -D=language=es --port 5500 --open-browser
# For English
sphinx-autobuild docs docs/_build/html/en -D=language=en --port 5500 --open-browser
```


## How to Contribute

1. Checkout the **main** branch.
2. Create a new branch with a descriptive name (e.g. schedule-task), from **main** branch.
3. Modify/create .rst/.md documentation files inside the **/docs** folder.
4. Perform a Pull Request from the new branch to the **main** branch.


## Generate translation files

``` bash
cd [your-projects-path]/pyplan/docs
# create POT files
make gettext
# create/update PO files for translations
sphinx-intl update -p _build/gettext -l en
# update PO files
sphinx-intl update -p _build/gettext
```
