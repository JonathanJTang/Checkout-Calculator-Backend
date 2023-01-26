ARG PYTHON_VERSION=3.8-slim-buster

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY . /code/

# should run `flyctl deploy --build-secret SECRET_KEY=[actual secret key] --build-secret DATABASE_URL=sqlite:///db.sqlite3`
#     --mount=type=secret,id=DATABASE_URL \
#     export DATABASE_URL="$(cat /run/secrets/DATABASE_URL)" && \

# code is in the server directory
RUN --mount=type=secret,id=SECRET_KEY \
    export SECRET_KEY="$(cat /run/secrets/SECRET_KEY)" && \
    cd server && \
    python manage.py collectstatic --noinput && \
    python manage.py makemigrations --noinput && \
    python manage.py migrate

EXPOSE 8000

# replace server.wsgi with <project_name>.wsgi
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "--pythonpath", "server", "server.wsgi"]
