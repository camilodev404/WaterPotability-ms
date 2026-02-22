from pydantic import BaseModel, ConfigDict, Field

from src.core.feature_mapping import ENG_TO_MODEL_COLS


class PredictRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    ph: float = Field(..., ge=0, le=14)
    hardness: float = Field(..., alias="Hardness")
    solids: float = Field(..., alias="Solids")
    chloramines: float = Field(..., alias="Chloramines")
    sulfate: float = Field(..., alias="Sulfate")
    conductivity: float = Field(..., alias="Conductivity")
    organic_carbon: float = Field(..., alias="Organic_carbon")
    trihalomethanes: float = Field(..., alias="Trihalomethanes")
    turbidity: float = Field(..., alias="Turbidity")

    def to_model_payload(self) -> dict:
        return {
            ENG_TO_MODEL_COLS["ph"]: self.ph,
            ENG_TO_MODEL_COLS["Hardness"]: self.hardness,
            ENG_TO_MODEL_COLS["Solids"]: self.solids,
            ENG_TO_MODEL_COLS["Chloramines"]: self.chloramines,
            ENG_TO_MODEL_COLS["Sulfate"]: self.sulfate,
            ENG_TO_MODEL_COLS["Conductivity"]: self.conductivity,
            ENG_TO_MODEL_COLS["Organic_carbon"]: self.organic_carbon,
            ENG_TO_MODEL_COLS["Trihalomethanes"]: self.trihalomethanes,
            ENG_TO_MODEL_COLS["Turbidity"]: self.turbidity,
        }


class PredictResponse(BaseModel):
    prediction: int
    label: str


class HealthResponse(BaseModel):
    status: str
    app: str
    version: str


class MetricsResponse(BaseModel):
    model_id: str
    model_version: str
    accuracy: float
    precision: float
    recall: float
    f1_score: float
