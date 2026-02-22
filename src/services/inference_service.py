from typing import Any, Dict

import pandas as pd

from src.api.schemas.schema import PredictRequest, PredictResponse


class InferenceService:
    def __init__(self, model: Any) -> None:
        self.model = model

    def predict(self, payload: PredictRequest) -> PredictResponse:
        features: Dict[str, float] = payload.to_model_payload()
        frame = pd.DataFrame([features])
        pred = self.model.predict(frame)
        result = int(pred[0])
        label = "Potable" if result == 1 else "Not Potable"
        return PredictResponse(prediction=result, label=label)
