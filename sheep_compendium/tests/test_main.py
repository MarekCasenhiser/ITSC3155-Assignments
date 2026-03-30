from fastapi.testclient import TestClient


from main import app

client = TestClient(app)


def test_read_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == {
        "id" : 1,
        "name" : "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():
    # TODO: Prepare the new sheep data in a dictionary format
    response = client.get("/sheep/1")
    # TODO: Assert that the response status code is 201
    assert response.status_code ==201
    assert response.json() == {
        "id" : 1,
        "name" : "Blondie",
        "breed" : "Polyplay",
        "sex" : "ram"
    }
    # TODO: Assert that the response JSON matches the new sheep data
    # TODO: Verify that the sheep was actually added to the database by retrieveing the new sheep by ID.
    # TODO: Include an assert statement to see if the new data can be retrieved.
