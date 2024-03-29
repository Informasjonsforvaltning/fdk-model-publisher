FROM python:3.11

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install "poetry==1.5.1"
COPY poetry.lock pyproject.toml /app/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --only main --no-interaction --no-ansi

ADD src /app/src

# Setting PYTHONUNBUFFERED to a non empty value ensures that
# the python output is sent straight to terminal (e.g. your container log)
# without being first buffered and that you can see the output
# of your application (e.g. django logs) in real time.
# This also ensures that no partial output is held in a buffer
# somewhere and never written in case the python application crashes.
ENV PYTHONUNBUFFERED 1

EXPOSE 8080

CMD gunicorn --chdir src "fdk_model_publisher:create_app" --config=src/fdk_model_publisher/gunicorn_config.py --worker-class aiohttp.GunicornWebWorker --timeout 1800
