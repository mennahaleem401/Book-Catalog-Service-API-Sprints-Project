from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200

def test_add_book():
    response = client.post(
        "/books",
        json={
            "title": "Clean Code",
            "author": "Robert Martin",
            "isbn": "123456"
        }
    )
    assert response.status_code == 200