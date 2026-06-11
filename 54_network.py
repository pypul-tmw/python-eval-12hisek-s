import requests

url = "https://www.google.com"

try:
    response = requests.get(url)
    response.raise_for_status()#checks if request was successful?

except requests.exceptions.RequestException as e:
    print("Error:",e)
else:
    print("Response code:",response.status_code)