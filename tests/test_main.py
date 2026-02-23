from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_auth_protected_route_without_token():
    response = client.get("/my-portfolio")
    assert response.status_code == 401

def test_login_wrong_password():
    response = client.post(
        "/login",
        data={"username": "test@example.com", "password": "wrongpassword"}
    )
    assert response.status_code == 403