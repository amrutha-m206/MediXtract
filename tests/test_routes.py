import pytest
from backend.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# Test for homepage route
def test_homepage(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Search" in res.data  # Check if the Search form is present


# Test for search route
def test_search_route(client):
    # Simulating a POST request to /search route
    res = client.post("/search", data={"query": "neuroscience"})
    assert res.status_code == 200
    assert (
        b"results" in res.data or b"Summary" in res.data
    )  # Ensure the response contains the results or summary


# Test for summarize route
def test_summarize_route(client):
    # Simulating a POST request to /summarize route
    # Assume you have a valid paper_id (replace with actual ID)
    res = client.post("/summarize", data={"paper_id": "2311.02704"})
    assert res.status_code == 200
    assert (
        b"Summary" in res.data
    )  # Check if the summary content is present in the response
