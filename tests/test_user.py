import pytest
import requests
import requests_mock

@pytest.fixture
def api_url():
    return "http://127.0.0.1:8000/users"

def test_empty_response_with_401(api_url, mocker):
    params = {
        "username": "admin",
        "password": "admin"
    }

    with requests_mock.Mocker() as mock_request:
        mock_request.get(api_url, status_code=401, text='')

        response = requests.get(api_url, params=params)
    
    assert response.status_code == 401
    assert response.text == ''

def test_empty_response_with_200(api_url, mocker):
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    with requests_mock.Mocker() as mock_request:
        mock_request.get(api_url, status_code=200, text='')

        response = requests.get(api_url, params=params)
    
    assert response.status_code == 200
    assert response.text == ''
