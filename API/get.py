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
    
def volatility(): 
    x = 'AMD'
    url = "https://spawnerapi.com/volatility/" + x + "/" + token
    response = requests.get(url)
    print(response.text)

def expected_returns(): 
    x = 'AMD'
    url = "https://spawnerapi.com/expected-return/" + x + "/" + token
    response = requests.get(url)
    print(response.text)

def max_drawdown(): 
    x = 'AMD'
    url = "https://spawnerapi.com/max-drawdown/" + x + "/" + token
    response = requests.get(url)
    print(response.text)

def sharpe(): 
    x = 'AMD'
    url = "https://spawnerapi.com/sharpe/" + x + "/" + token
    response = requests.get(url)
    print(response.text)

def calmar(): 
    x = 'AMD'
    url = "https://spawnerapi.com/calmar/" + x + "/" + token
    response = requests.get(url)
    print(response.text)

def sortino(): 
    x = 'AMD'
    url = "https://spawnerapi.com/sortino/" + x + "/" + token
    response = requests.get(url)
    print(response.text)

def value_at_risk(): 
    x = 'AMD'
    url = "https://spawnerapi.com/value-at-risk/" + x + "/" + token
    response = requests.get(url)
    print(response.text)

def kelly_criterion(): 
    x = 'AMD'
    url = "https://spawnerapi.com/kelly-criterion/" + x + "/" + token
    response = requests.get(url)
    print(response.text)

def implied_volatility(): 
    x = 'AMD'
    url = "https://spawnerapi.com/implied-volatility/" + x + "/" + token
    response = requests.get(url)
    print(response.text)

