import requests
import json


# Replace with your API Key, get key from https://spawner.ai
api_key = '' 

###### POST ENDPOINTS #######
def clean(): 
    text = 'here is $ ? dir/ty teXt. .'
    url = 'https://spawnerapi.com/clean/' + token
    data = {'text': text}
    headers = {'Content-type': 'application/json'}

    x = requests.post(url, data=json.dumps(data), headers=headers)
    print(x.text)

def sentiment(): 
    text = 'This api is so good.'
    url = 'https://spawnerapi.com/sentiment/' + token
    data = {'text': text}
    headers = {'Content-type': 'application/json'}

    x = requests.post(url, data=json.dumps(data), headers=headers)
    print(x.text)

def understand(): 
    text = 'What are the keywords in this phrase?'
    url = 'https://spawnerapi.com/understand/' + token
    data = {'text': text}
    headers = {'Content-type': 'application/json'}

    x = requests.post(url, data=json.dumps(data), headers=headers)
    print(x.text)

def answer(): 
    text = 'What is the p/e ratio of apple?'
    url = 'https://spawnerapi.com/answer/' + token
    data = {'text': text}
    headers = {'Content-type': 'application/json'}

    x = requests.post(url, data=json.dumps(data), headers=headers)
    print(x.text)

def forecast(): 
    dates = '12-01-01, 12-01-02'
    values = '1, 2'
    periods = '3'
    url = 'https://spawnerapi.com/forecast/' + token
    data = {'dates': dates, 'values': values, 'periods': periods}
    headers = {'Content-type': 'application/json'}

    x = requests.post(url, data=json.dumps(data), headers=headers)
    print(x.text)

clean()
