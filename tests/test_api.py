# tests/test_api.py

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Sui Smart Contract Chatbot API!"}

def test_generate_endpoint():
    # Here we test the /api/generate endpoint.
    payload = {
        "prompt": "Create a Sui smart contract that mints tokens."
    }
    response = client.post("/api/generate", json=payload)
    assert response.status_code == 200
    # We check for the keys in the response (contract_code and message)
    data = response.json()
    assert "contract_code" in data
    assert "message" in data

def test_invalid_generate_endpoint():
    # Here we test the /api/generate endpoint with invalid data.
    payload = {
        "invalid_key": "This should fail."
    }
    response = client.post("/api/generate", json=payload)
    assert response.status_code == 422
    # We check for the error message in the response
    data = response.json()
    assert "detail" in data

def test_missing_prompt_generate_endpoint():
    # Here we test the /api/generate endpoint with a missing prompt.
    payload = {}
    response = client.post("/api/generate", json=payload)
    assert response.status_code == 422
    # We check for the error message in the response
    data = response.json()
    assert "detail" in data