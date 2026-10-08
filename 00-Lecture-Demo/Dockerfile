FROM python:3.12.8-slim

ARG DEBIAN_FRONTEND=noninteractive

ENV PYTHONUNBUFFERED=1
ENV WRITEPYTHONBYTECODE=1

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry \
    && poetry install

COPY api/ api/

EXPOSE 8000

ENTRYPOINT [ "poetry", "run" ]

CMD ["uvicorn", "api.fast:app", "--host", "0.0.0.0", "--port", "8000"]
