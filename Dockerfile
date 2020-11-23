FROM python:3.8

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install "poetry==1.1.3"
COPY poetry.lock pyproject.toml /app/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

ADD src /app/src

EXPOSE 8080

CMD gunicorn --chdir src "app:create_app" --config=src/fdk_model_publisher/gunicorn_config.py --worker-class aiohttp.GunicornWebWorker
