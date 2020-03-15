import requests 
import json 


token = ''

url = "https://spawnerapi.com/fundamentals/" + token

response = requests.get(url)
print(response.json())
