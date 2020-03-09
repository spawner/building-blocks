import requests 
import json 
import pandas as pd


# You need an API Key for the API to work. Get key from https://spawner.ai
api_key = 'sp_42ac416e99569d5ea3281013db5a9f33'
question = 'what is the revenue of apple and ge'

url = "http://spawnerapi.com/answer/" + question + "/" + api_key

response = requests.get(url)
response_text = json.loads(response.text) 

# Loop over JSON and send to lists
stocks = []
data_type = []
data = []
for i in response_text:
    stocks.append(i['x_axis'])
    data_type.append(i['chart_title'])
    data.append(i['data'])

print(stocks)
print(data_type)
print(data)

# Add to dataframe and output to .csv
df = pd.DataFrame(list(zip(stocks, data_type, data)), columns =['Stock', 'Type', 'Data']) 
print(df) 

df.to_csv('data/answer_data.csv', index=False)

