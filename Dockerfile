FROM python:3.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY . .
RUN uv sync --frozen

# Ajout du chemin pour que le package 'app' soit reconnu
ENV PYTHONPATH="."

CMD ["uv", "run", "app/main.py"]