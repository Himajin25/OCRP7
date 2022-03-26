""" File containing the tests for the views.py file """
def test_index(client):
    response_get = client.get("/")
    response_post = client.post("/")
    assert response_get.status_code == 200
    assert response_post.status_code == 405


def test_api(client):
    response = client.get("/api")
    assert response.status_code == 500

# class TestGrandPyAPI:
#     def test_address_in_response(self):
#         assert 
#         pass
#     def test_map_url_in_response(self):
#         pass
#     def test_wiki_in_response(self):
#         pass