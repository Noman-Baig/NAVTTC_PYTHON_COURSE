import requests

url = "https://api.spacexdata.com/v4/launches/latest"
response = requests.get(url)

data = response.json()
print(data)
