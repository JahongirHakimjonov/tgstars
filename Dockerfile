FROM python:3.12-slim

# Poetry ni o‘rnatamiz
ENV POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s $POETRY_HOME/bin/poetry /usr/local/bin/poetry && \
    apt-get purge -y curl && \
    apt-get autoremove -y && \
    apt-get clean

# Loyihani ko‘chirib o‘tkazamiz
WORKDIR /app
COPY pyproject.toml poetry.lock* /app/

# Dependencies'larni o‘rnatamiz
RUN poetry install --no-root

# Barcha fayllarni nusxalaymiz
COPY . .

# Uvicorn orqali ishga tushiramiz
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
