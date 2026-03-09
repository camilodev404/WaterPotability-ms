from fastapi import APIRouter, Depends, Request

from src.api.controllers.controller import build_metrics
from src.api.schemas.schema import HealthResponse, MetricsResponse, PredictRequest, PredictResponse
from src.core.config import Settings, get_settings
from src.services.inference_service import InferenceService

router = APIRouter(prefix="/api/v1", tags=["water-potability"])


def get_inference_service(request: Request) -> InferenceService:
    return request.app.state.inference_service


@router.get("/health", response_model=HealthResponse)
def health(settings: Settings = Depends(get_settings)) -> HealthResponse:
    return HealthResponse(status="ok", app=settings.app_name, version=settings.app_version)


@router.get("/metrics", response_model=MetricsResponse)
def metrics(
    request: Request,
    settings: Settings = Depends(get_settings),
) -> MetricsResponse:
    return build_metrics(
        models=request.app.state.inference_service.models,
        model_paths=request.app.state.model_paths,
        csv_path=settings.metrics_csv_path,
    )


@router.post("/predict", response_model=PredictResponse)
def predict(
    payload: PredictRequest,
    service: InferenceService = Depends(get_inference_service),
) -> PredictResponse:
    return service.predict(payload)
