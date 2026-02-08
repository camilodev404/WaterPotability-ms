# 🚀 Water Potability API

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![API](https://img.shields.io/badge/API-REST-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-Inference-green)

API encargada de **servir las inferencias del modelo de Machine Learning** para la predicción de potabilidad del agua.

Este repositorio contiene únicamente:

✅ Lógica del API  
✅ Carga del modelo entrenado  
✅ Endpoints de inferencia  
✅ Validación de datos  


---

# 👥 Integrantes del Proyecto


- Cristian Camilo Nino Rincon
- Nombre Apellido
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
```


---

# ⚙️ Tecnologías

- Python
- FastAPI / Flask
- Pydantic
- Uvicorn / Gunicorn
- Docker
---


# 🤖 Integración con el Modelo

El modelo entrenado proviene del repositorio de Machine Learning.

Proceso esperado:

1. Exportar modelo (`.pkl`, `.joblib`, etc.)
2. Colocar artefacto en `/models`
3. Cargar modelo al iniciar la API

```python
# Ejemplo conceptual
model = load_model("models/model.joblib")