FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        pipenv postgresql-client
COPY ./Pipfile /Pipfile
COPY ./Pipfile.lock /Pipfile.lock
RUN pipenv install --system
WORKDIR /app
COPY ./django_app /app