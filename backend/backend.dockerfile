FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app/

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./app/pyproject.toml ./app/poetry.lock* /app/


RUN apt-get clean && apt-get update && apt-get install libsm6 libxext6  -y
RUN apt-get install libzbar0 -y
RUN mkdir /requirements
COPY ./app/requirements.txt /requirements
RUN pip install -r /requirements/requirements.txt

COPY ./app /app

ENV PYTHONPATH=/app