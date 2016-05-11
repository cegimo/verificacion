# verificacion
Verificación y desarrollo de programas

## Setup

1. Clone the repo
2. Be sure you have installed [virtualenv](https://virtualenv.pypa.io/en/latest/) in your machine:
```
pip install virtualenv
```
3. Install and active the virtualenv for your project 
```
rm -rf venv
virtualenv venv
source /venv/bin/activate
```
4. Install the requirements into your project
```
pip install -r requirements
```

## Run Tests
```
venv/bin/py.test tests
```

## Pylint
```
venv/bin/pylint ahorcado
```
