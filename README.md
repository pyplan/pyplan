# ![Pyplan](./docs/images/logo.png)

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

1. Update the branch of the version to be documented
2. Create a new branch with a descriptive name (e.g. schedule-task), based on the branch of the version that you want to document.
3. Modify/create documentation files inside the /docs folder
4. Perform a Pull Request from the new branch to the branch of the version to be modified
