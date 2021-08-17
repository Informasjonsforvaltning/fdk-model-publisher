# fdk-model-publisher
Transforms models included in dataservice-descriptions to modelldcat-ap-no compliant models and expose the collection

## Develop and run locally
### Requirements
- [pyenv](https://github.com/pyenv/pyenv) (recommended)
- [poetry](https://python-poetry.org/)
- [nox](https://nox.thea.codes/en/stable/)
- [nox-poetry](https://pypi.org/project/nox-poetry/)

### Install software:
```
% git clone https://github.com/Informasjonsforvaltning/fdk-model-publisher.git
% cd fdk-model-publisher
% pyenv install 3.8.6
% pyenv local 3.8.6
% pip install poetry==1.1.3
% pip install nox==2020.12.31
% pip install nox-poetry==0.8.4
% poetry install
```
### Environment variables
To run the service locally, you need to supply a set of environment variables. A simple way to solve this is to supply a .env file in the root directory.

```
FDK_DATASERVICE_HARVESTER_URI=https://dataservices.staging.fellesdatakatalog.digdir.no
```
### Running the API locally
 Start the endpoint:
```
% poetry shell
% FLASK_APP=fdk_model_publisher FLASK_ENV=development flask run --port=8080
```
## Running the API in a wsgi-server (gunicorn)
```
% poetry shell
% gunicorn  --chdir src "fdk_model_publisher:create_app()"  --config=src/fdk_model_publisher/gunicorn_config.py
```
## Running the wsgi-server in Docker
To build and run the api in a Docker container:
```
% docker build -t digdir/fdk-model-publisher:latest .
% docker run --env-file .env -p 8080:8080 -d digdir/fdk-model-publisher:latest
```
The easier way would be with docker-compose:
```
docker-compose up --build
```
## Running tests
We use [pytest](https://docs.pytest.org/en/latest/) for contract testing.

To run linters, checkers and tests:
```
% nox
```

## PyCharm

### interpreter
Ctrl+Alt+S -> Project -> python interpreter -> cog by dropdown -> Add -> Poetry Environment -> set 'python3.9' from '.../.pyenv/shims/' as Base interpreter and set 'poetry' from '.../.pyenv/shims/' as Poetry executable.

### pytest
Ctrl+Alt+S -> Tools -> Python integrated tools -> Testing -> set 'pytest' as Default test runner
