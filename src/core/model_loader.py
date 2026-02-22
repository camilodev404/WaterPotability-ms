from pathlib import Path
from typing import Any

import mlflow.pyfunc


class ModelLoaderError(RuntimeError):
    pass


def load_model(model_path: str) -> Any:
    resolved = Path(model_path).resolve()
    if not resolved.exists():
        raise ModelLoaderError(f"Model path does not exist: {resolved}")

    try:
        return mlflow.pyfunc.load_model(str(resolved))
    except Exception as exc:  # pragma: no cover
        raise ModelLoaderError(f"Failed to load model from {resolved}: {exc}") from exc
