FROM python:3.10

ENV PYTHONUNBUFFERED 1

EXPOSE 8501

WORKDIR /app

COPY requirements.txt /tmp/requirements

COPY ./app /app

RUN python -m venv /venv && \
    /venv/bin/pip install -r /tmp/requirements && \
    rm -rf /tmp

ENV PATH="/venv/bin:$PATH"

CMD ["streamlit", "run", "main.py", "--server.address=0.0.0.0"]
