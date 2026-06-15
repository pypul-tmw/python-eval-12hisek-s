from unittest.mock import MagicMock

def test_get_weather(mocker):

    # 1. fake response object
    mock_response = MagicMock()

    # 2. fake API JSON response
    mock_response.json.return_value = {
        "city": "Mumbai",
        "temp": 30
    }

    # 3. replace requests.get with fake
    mocker.patch("requests.get", return_value=mock_response)

    # 4. import function
    from weather_app import get_weather

    # 5. call function
    result = get_weather("Mumbai")

    # 6. verify output
    assert result["temp"] == 30
    assert result["city"] == "Mumbai"