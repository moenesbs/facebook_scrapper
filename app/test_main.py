from main import app
import json
from fastapi.testclient import TestClient


client = TestClient(app)


def test_code_main():
    response = client.post("/scrap")
    assert response.status_code == 200

def test_response_keys():
    response = client.post("/scrap").json()
    response = json.loads(response["data"])
    keys = ["post_type","post_link","post_description","post_date","comments_number","comments","reactions_number","reaction_details"]
    good_format = True
    for post in response:
        assert list(post.keys()).sort() == keys.sort()



def test_response_values():
    response = client.post("/scrap").json()
    response = json.loads(response["data"])
    for post in response:
        assert None not in list(post.values())