from typing import Any, Dict

import pandas as pd

from src.api.schemas.schema import PredictRequest, PredictResponse


class InferenceService:
    def __init__(self, models: Dict[str, Any], default_model_name: str = "decision_tree") -> None:
        self.models = models
        self.default_model_name = default_model_name if default_model_name in models else next(iter(models))

    def predict(self, payload: PredictRequest) -> PredictResponse:
        features: Dict[str, float] = payload.to_model_payload()
        frame = pd.DataFrame([features])
        model_name = payload.model_name if payload.model_name in self.models else self.default_model_name
        model = self.models[model_name]
        pred = model.predict(frame)
        result = int(pred[0])
        label = "Potable" if result == 1 else "Not Potable"
        return PredictResponse(model_name=model_name, prediction=result, label=label)
