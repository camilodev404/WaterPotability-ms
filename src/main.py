from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes.route import router as api_router
from src.core.config import get_settings
from src.core.model_loader import load_model
from src.services.inference_service import InferenceService

settings = get_settings()
model = load_model(settings.model_path)
inference_service = InferenceService(model)

app = FastAPI(title=settings.app_name, version=settings.app_version)
app.state.inference_service = inference_service

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict:
    return {"message": "Water Potability API is running"}


@app.get("/health")
def root_health() -> dict:
    return {"status": "ok"}


app.include_router(api_router)
