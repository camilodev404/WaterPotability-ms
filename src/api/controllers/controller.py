from pathlib import Path
from typing import Any, Tuple

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

from src.api.schemas.schema import MetricsResponse
from src.core.feature_mapping import ENG_TO_MODEL_COLS


def _read_mlmodel_identifiers(model_path: str) -> Tuple[str, str]:
    mlmodel_path = Path(model_path) / "MLmodel"
    if not mlmodel_path.exists():
        return ("unknown", "unknown")

    model_id = "unknown"
    mlflow_version = "unknown"

    for line in mlmodel_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("model_id:"):
            model_id = line.split(":", 1)[1].strip()
        if line.startswith("mlflow_version:"):
            mlflow_version = line.split(":", 1)[1].strip()

    return (model_id, mlflow_version)


def build_metrics(model: Any, model_path: str, csv_path: str) -> MetricsResponse:
    data_path = Path(csv_path)
    if not data_path.exists():
        raise FileNotFoundError(f"Metrics dataset not found: {data_path}")

    df = pd.read_csv(data_path)

    expected_features = list(ENG_TO_MODEL_COLS.keys())
    missing = [col for col in expected_features if col not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns in metrics CSV: {missing}")
    if "Potability" not in df.columns:
        raise ValueError("Missing expected target column in metrics CSV: Potability")

    eval_df = df[expected_features + ["Potability"]].dropna().copy()
    if eval_df.empty:
        raise ValueError("No rows available to compute metrics after dropping null values")

    X = eval_df[expected_features].rename(columns=ENG_TO_MODEL_COLS)
    y_true = eval_df["Potability"].astype(int)
    y_pred = pd.Series(model.predict(X)).astype(int)

    model_id, model_version = _read_mlmodel_identifiers(model_path)

    return MetricsResponse(
        model_id=model_id,
        model_version=model_version,
        accuracy=float(accuracy_score(y_true, y_pred)),
        precision=float(precision_score(y_true, y_pred, zero_division=0)),
        recall=float(recall_score(y_true, y_pred, zero_division=0)),
        f1_score=float(f1_score(y_true, y_pred, zero_division=0)),
    )
