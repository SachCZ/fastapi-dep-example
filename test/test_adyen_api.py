from fastapi.testclient import TestClient
from app.adyen_client import AdyenClient
from app.main import app

client = TestClient(app)


class FakeClient:
    def get_items(self):
        return ["testing", "items"]


app.dependency_overrides[AdyenClient] = FakeClient


def test_read_main():
    response = client.get("/api/items")
    assert response.status_code == 200
    assert response.json() == ["testing", "items"]
