from unittest.mock import MagicMock

def test_download_data(mocker):
    mock_response = MagicMock()
    mock_response.json.return_value = {'data': 'Hello, World!'}

    mocker.patch('requests.get', return_value=mock_response)

    from app import download_data
    data = download_data()

    print("data:", data)

    assert data == {'data': 'Hello, World!'}