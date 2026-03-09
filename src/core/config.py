from functools import lru_cache
from pathlib import Path
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Water Potability API"
    app_version: str = "1.0.0"
    model_path: str = "models/water_potability_model"
    model_path_nn: str = "models/water_potability_model_nn"
    default_model_name: str = "decision_tree"
    metrics_csv_path: str = "../WaterPotability/data/raw/water_potability.csv"
    cors_origins: List[str] = Field(default_factory=lambda: ["http://localhost:4200"])

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def absolute_model_path(self) -> Path:
        return Path(self.model_path).resolve()

    @property
    def absolute_model_path_nn(self) -> Path:
        return Path(self.model_path_nn).resolve()


@lru_cache

def get_settings() -> Settings:
    return Settings()
