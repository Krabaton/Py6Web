import os

import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)
os.environ["ENV_APP"] = "stage"  # development production


def test_read_main():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_token():
    response = client.post("/token", data={"username": "krabat@ex.ua", "password": "567234"})
    email = response.json()["user_email"]
    assert response.status_code == 200
    assert email == "krabat@ex.ua"


@pytest.fixture
def get_token(scope="module"):
    response = client.post("/token", data={"username": "krabat@ex.ua", "password": "567234"})
    return response.json()["access_token"]


def test_notes(get_token):
    response = client.get("/notes", headers={'Authorization': f'Bearer {get_token}'})
    print(response.json())
    assert len(response.json()) > 0
    assert response.status_code == 200
