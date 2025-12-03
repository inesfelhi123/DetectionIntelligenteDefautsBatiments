from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_endpoint():
    with open("tests/algae.jpg", "rb") as f:
        response = client.post("/predict/", files={"image": f})
    print(response.json()) 
    assert response.status_code == 200
    assert "class" in response.json()
    assert "confidence" in response.json()
