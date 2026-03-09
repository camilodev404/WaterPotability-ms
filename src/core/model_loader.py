from pathlib import Path
from typing import Any, Dict

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


def load_models(model_paths: Dict[str, str]) -> Dict[str, Any]:
    loaded: Dict[str, Any] = {}
    missing: Dict[str, str] = {}

    for model_name, model_path in model_paths.items():
        try:
            loaded[model_name] = load_model(model_path)
        except ModelLoaderError:
            missing[model_name] = str(Path(model_path).resolve())

    if not loaded:
        details = ", ".join([f"{k}={v}" for k, v in missing.items()]) or "none"
        raise ModelLoaderError(f"No models could be loaded. Missing/invalid paths: {details}")

    return loaded
