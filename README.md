# fdk-model-publisher

Transforms models included in dataservice-descriptions to modelldcat-ap-no compliant models and expose the collection

## Develop and run locally

### Requirements

- [pyenv](https://github.com/pyenv/pyenv) (recommended)
- [poetry](https://python-poetry.org/)
- [nox](https://nox.thea.codes/en/stable/)
- [nox-poetry](https://pypi.org/project/nox-poetry/)

### Install software

```Shell
% git clone https://github.com/Informasjonsforvaltning/fdk-model-publisher.git
% cd fdk-model-publisher
% pyenv install 3.10.10
% pyenv local 3.10.10
% pip install poetry==1.4.2
% pip install nox==2021.11.21
% pip install nox-poetry==1.0.2
% poetry install
```

### Environment variables

To run the service locally, you need to supply a set of environment variables. A simple way to solve this is to supply a .env file in the root directory.

```Shell
FDK_DATASERVICE_HARVESTER_URI=https://dataservices.staging.fellesdatakatalog.digdir.no
```

### Running the API locally

Start the endpoint:

```Shell
% poetry shell
% FLASK_APP=fdk_model_publisher FLASK_ENV=development flask run --port=8080
```

## Running the API in a wsgi-server (gunicorn)

```Shell
% poetry shell
% gunicorn  --chdir src "fdk_model_publisher:create_app()"  --config=src/fdk_model_publisher/gunicorn_config.py
```

## Running the wsgi-server in Docker

To build and run the api in a Docker container:

```Shell
% docker build -t digdir/fdk-model-publisher:latest .
% docker run --env-file .env -p 8080:8080 -d digdir/fdk-model-publisher:latest
```

The easier way would be with docker-compose:

```Shell
docker-compose up --build
```

## Running tests

We use [pytest](https://docs.pytest.org/en/latest/) for contract testing.

To run linters, checkers and tests:

```Shell
% nox
```

## PyCharm

### interpreter

Ctrl+Alt+S -> Project -> python interpreter -> cog by dropdown -> Add -> Poetry Environment -> set 'python3.9' from '.../.pyenv/shims/' as Base interpreter and set 'poetry' from '.../.pyenv/shims/' as Poetry executable.

### pytest

Ctrl+Alt+S -> Tools -> Python integrated tools -> Testing -> set 'pytest' as Default test runner
