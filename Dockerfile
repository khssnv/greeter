FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/
COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv && pipenv install

COPY ./app/ /app/

EXPOSE 80
