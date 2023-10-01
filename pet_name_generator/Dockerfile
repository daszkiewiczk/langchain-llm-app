FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /tmp/requirements

COPY ./app /app

RUN python -m venv /venv && \
    /venv/bin/pip install -r /tmp/requirements && \
    rm -rf /tmp

ENV PATH="/venv/bin:$PATH"

CMD ["python", "main.py"]
