# Water Potability API

Microservicio FastAPI para inferencia del modelo de potabilidad de agua.

## Estructura

- `src/main.py`: arranque de FastAPI.
- `src/api/routes/route.py`: rutas `/api/v1`.
- `src/api/schemas/schema.py`: contratos request/response.
- `src/services/inference_service.py`: lógica de inferencia.
- `src/core/model_loader.py`: carga del modelo MLflow.
- `models/water_potability_model`: artefacto del modelo (`MLmodel`, `model.pkl`, etc.).

## Requisitos

- Python 3.12+

## Configuración local


# 👥 Integrantes del Proyecto


- Cristian Camilo Nino Rincon
- Sandra Milena Pantoja Cárdenas
- Nombre Apellido
- Nombre Apellido

---

# 📌 Descripción General

Esta API forma parte de una arquitectura modular compuesta por tres repositorios principales:

- 🤖 Modelo → Entrenamiento y datos (https://github.com/camilodev404/WaterPotability)
- 🚀 API (https://github.com/camilodev404/WaterPotability-ms) → Servir inferencias
- 📊 Frontend / Dashboard → Visualización y consumo del API (https://github.com/camilodev404/WaterPotability-dashboard)

El objetivo principal es exponer endpoints REST que permitan:

- Enviar variables fisicoquímicas del agua
- Obtener predicciones de potabilidad en tiempo real

---

# 🧱 Arquitectura del Proyecto

```
project-root/
│
├── src/
│ ├── api/
│ │ ├── routes/
│ │ ├── schemas/
│ │ └── controllers/
│ │
│ ├── core/
│ │ ├── config.py
│ │ └── model_loader.py
│ │
│ ├── services/
│ │ └── inference_service.py
│ │
│ └── main.py
│
├── models/ # Modelo exportado (ej: .pkl / .joblib)
├── tests/
├── requirements.txt
└── README.md
=======
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
>>>>>>> 024c7ed (first version ms)
```

## Copiar modelo entrenado

Desde el root del monorepo:

```bash
mkdir -p WaterPotability-ms/models/water_potability_model
cp -r WaterPotability/notebooks/mlruns/1/models/m-1ccb4a99340344b4a23ab8657794666a/artifacts/* \
  WaterPotability-ms/models/water_potability_model/
```

## Ejecutar API

```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

## Endpoints

- `GET /health`
- `GET /api/v1/health`
- `GET /api/v1/metrics` (calcula metricas reales sobre `METRICS_CSV_PATH`)
- `POST /api/v1/predict`

### Ejemplo `POST /api/v1/predict`

```json
{
  "ph": 7.2,
  "Hardness": 204.0,
  "Solids": 20791.0,
  "Chloramines": 7.3,
  "Sulfate": 368.5,
  "Conductivity": 564.3,
  "Organic_carbon": 10.4,
  "Trihalomethanes": 86.9,
  "Turbidity": 2.9
}
```
