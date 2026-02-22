from pathlib import Path

from fastapi.testclient import TestClient


def test_health_endpoint() -> None:
    if not Path("models/water_potability_model").exists():
        return

    from src.main import app

    client = TestClient(app)
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
