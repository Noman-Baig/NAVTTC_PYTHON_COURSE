import requests

url = "https://api.spacexdata.com/v4/launches/latest"
response = requests.get(url)

data = response.json()
print(data)


# try 2nd

import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)
data = response.json()

print(data)
