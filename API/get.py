import requests 
import json 


# Replace with your token. You can get a token at https://spawner.ai
token = ''

####### GET ENDPOINTS ########
def fundamentals(): 
    url = "https://spawnerapi.com/fundamentals/" + token
    response = requests.get(url)
    print(response.json())

def portfolio(): 
    tickers = 'ge, aapl'
    url = "https://spawnerapi.com/portfolio/" + tickers + '/' + token
    response = requests.get(url)
    print(response.json())

def backtest(): 
    start = '2012-02-23'
    end = '2012-02-24'
    tickers = 'ge, aapl'
    url = "https://spawnerapi.com/backtest/" + start + "/" + end + "/" + tickers + "/" + token
    response = requests.get(url)
    print(response.json())

def ta(): 
    ticker = 'aapl'
    url = "https://spawnerapi.com/ta/" + ticker + "/" + token
    response = requests.get(url)
    print(response.json())

def basic_stats(): 
    x = '1,2,3'
    url = "https://spawnerapi.com/basic-stats/" + x + "/" + token
    response = requests.get(url)
    print(response.json())

#fundamentals()
#portfolio()
#backtest() 
#ta()
#basic_stats()
