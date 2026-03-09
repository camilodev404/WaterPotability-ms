FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY WaterPotability-ms/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

COPY WaterPotability-ms/src /app/src
COPY WaterPotability-ms/scripts /app/scripts
COPY WaterPotability-ms/data /app/data
COPY WaterPotability-ms/.env.example /app/.env.example
COPY WaterPotability-ms/models/water_potability_model /app/models/water_potability_model
COPY WaterPotability-ms/models/water_potability_model_nn /app/models/water_potability_model_nn

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
