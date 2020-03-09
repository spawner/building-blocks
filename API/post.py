import requests
import json
import base64
import pandas as pd 
from datetime import datetime

# Replace with your API Key, get key from https://spawner.ai
api_key = 'sp_42ac416e99569d5ea3281013db5a9f33' 

# Replace with whatever URL you want to use
url = "http://spawnerapi.com/image-classifier/" + api_key

# prepare headers for http request, headers will differ depending on endpoint 
content_type = 'image/jpeg'
headers = {'content-type': content_type}

# Base64 encode a PNG/JPEG image
b64 = base64.b64encode(open('data/obelisk.jpg','rb').read())

response = requests.post(url, data=b64, headers=headers)
response_text = json.loads(response.text) 

# Loop over JSON and send to lists
class_membership = []
probability = []
time = []
for i in response_text:
    class_membership.append(i['class'])
    probability.append(i['probability'])
    time.append(str(datetime.now()))

print(class_membership)
print(probability)
print(time)

# Add to dataframe and output to .csv
df = pd.DataFrame(list(zip(class_membership, probability, time)), columns =['Class', 'Probability', 'Time']) 
print(df) 

df.to_csv('data/image_data.csv', mode='a', index=False)
