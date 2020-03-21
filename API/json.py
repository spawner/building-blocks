import requests 
import json 


# input your token here
token = 'sp_xxxxxxxxxxxxxxxxxxxxxxxxxxx'

text = 'revenue of boeing?'
url = 'https://spawnerapi.com/answer/' + token
data = {'text': text}
headers = {'Content-type': 'application/json'}

x = requests.post(url, data=json.dumps(data), headers=headers)
result = json.loads(x.text)
for i in result:
    print(i['text']) 
    
# The totalRevenue of Boeing Company (BA) is 17911000000.0
# The costOfRevenue of Boeing Company (BA) is 18703000000.0
