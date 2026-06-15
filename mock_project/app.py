from unittest.mock import MagicMock

import requests

def download_data():
    response = requests.get("https://google.com")
    return response.json()
