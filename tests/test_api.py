import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"
REQUEST_TIMEOUT = 10


def test_get_posts():
    response = requests.get(BASE_URL, timeout=REQUEST_TIMEOUT)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_post():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(BASE_URL, json=payload, timeout=REQUEST_TIMEOUT)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "foo"
    assert data["body"] == "bar"


def test_update_post():
    payload = {"title": "updated title"}
    response = requests.put(
        f"{BASE_URL}/1",
        json=payload,
        timeout=REQUEST_TIMEOUT,
    )
    assert response.status_code == 200
    assert response.json()["title"] == "updated title"


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/1", timeout=REQUEST_TIMEOUT)
    assert response.status_code == 200
