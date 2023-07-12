import pytest
import requests
import requests_mock

@pytest.fixture
def endpoint():
    return 'http://127.0.0.1:8000/users'

def test_empty_response_and_401(endpoint, mocker):
    params = {
        'username': 'admin',
        'password': 'admin'
    }

    with requests_mock.Mocker() as mock:
        mock.get(endpoint, status_code=401, text='')
        response = requests.get(endpoint, params=params)
        assert response.status_code == 401
        assert response.text == ''

def test_empty_response_and_200(endpoint, mocker):
    params = {
        'username': 'admin',
        'password': 'qwerty'
    }

    with requests_mock.Mocker() as mock:
        mock.get(endpoint, status_code=200, text='')
        response = requests.get(endpoint, params=params)
        assert response.status_code == 200
        assert response.text == ''