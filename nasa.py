import requests

api_key = "4psCXGThidWbigGXbIohQ4ClNXxs0SO82drn4EcZ"
url = "https://api.nasa.gov/planetary/apod"
params = {
    "api_key" : api_key
}

req = requests.get(url, params=params).json()
print(req["title"])
print(req["explanation"])