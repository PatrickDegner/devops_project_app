from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_say_hello():
    response = client.get("/hello/World")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_say_hello_other_name():
    response = client.get("/hello/TestUser")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello TestUser"}

def test_say_hello_empty_name():
    response = client.get("/hello/")
    assert response.status_code == 404

def test_say_hello_special_chars():
    response = client.get("/hello/User%20With%20Spaces")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello User With Spaces"}

def test_say_hello_long_name():
    long_name = "a" * 2000  # Very long name
    response = client.get(f"/hello/{long_name}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {long_name}"}