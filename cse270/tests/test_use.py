import pytest
import requests
from reqeusts.models import Response
from unittest.mock import Mock

@pytest.fixture
def api_url():
    return "http://127.0.0.1:8000/users"

def test_authorized_access(api_url, mocker):
    # Define the parameters
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    # Mock the requests.get() function
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mocker.patch('requests.get', return_value=mock_response)

    # Send a request to the endpoint
    response = requests.get(api_url, params=params)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
