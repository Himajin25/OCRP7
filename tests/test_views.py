""" File containing the tests for the views.py file """
def test_index(client):
    response_get = client.get("/")
    response_post = client.post("/")
    assert response_get.status_code == 200
    assert response_post.status_code == 405


def test_api(client):
    response = client.get("/api")
    assert response.status_code == 500

