from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes.route import router as api_router
from src.core.config import get_settings
from src.core.model_loader import load_models
from src.services.inference_service import InferenceService

settings = get_settings()
configured_model_paths = {
    "decision_tree": settings.model_path,
    "neural_network": settings.model_path_nn,
}
models = load_models(configured_model_paths)
model_paths = {name: configured_model_paths[name] for name in models}
inference_service = InferenceService(models=models, default_model_name=settings.default_model_name)

app = FastAPI(title=settings.app_name, version=settings.app_version)
app.state.inference_service = inference_service
app.state.model_paths = model_paths

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
