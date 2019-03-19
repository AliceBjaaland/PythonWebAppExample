import requests
import config

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units":"metric", "appid":config.appid}

response = requests.get(endpoint, params=payload)

response = requests.get(endpoint, params=payload)
data = response.json()

print (data['main'])
print (response.url)
print (response.status_code)
print (response.headers["content-type"])

print (response.text)
