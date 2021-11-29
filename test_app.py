import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_contact_page(client):
    reponse = client.get("/contact")
    assert reponse.status_code == 200
