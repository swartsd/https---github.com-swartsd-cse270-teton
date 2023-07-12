import pytest
import requests

def test_endpoint():
    # Make the HTTP request
    response = requests.get("http://127.0.0.1:8000/data/all")

    # Validate the response
    assert response.status_code == 200
    data = response.json()
    assert "businesses" in data
    assert isinstance(data["businesses"], list)
    assert len(data["businesses"]) > 0
    first_business = data["businesses"][0]
    assert isinstance(first_business, dict)
    assert "name" in first_business
    assert first_business["name"] == "Teton Elementary"
