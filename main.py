import ccxt
from ccxt import kucoin
import asyncio
from kucoin.client import Market
from kucoin.client import Trade
from kucoin.client import User
from flask import Flask, request
import json
from decimal import *

api_key = '63e0bc0e8f06ad0001ac4b4e'
api_secret = '8c5c0c9c-6a21-4c11-9680-9f5ebcdd3e45'
api_passphrase = 'iliketurtles'

exchange = ccxt.kucoin({
    'enableRateLimit': True,
    'api_key': '63e0bc0e8f06ad0001ac4b4e',
    'secret': '8c5c0c9c-6a21-4c11-9680-9f5ebcdd3e45',
    'password': 'iliketurtles'
})

#client = Market(url='https://api.kucoin.com')
clientTrade = Trade(key='63e0bc0e8f06ad0001ac4b4e', secret='8c5c0c9c-6a21-4c11-9680-9f5ebcdd3e45', passphrase='iliketurtles', is_sandbox=False, url='https://api.kucoin.com')
clientMarket = Market(key='63e0bc0e8f06ad0001ac4b4e', secret='8c5c0c9c-6a21-4c11-9680-9f5ebcdd3e45', passphrase='iliketurtles', is_sandbox=False, url='https://api.kucoin.com')
clientClient = User(key='63e0bc0e8f06ad0001ac4b4e', secret='8c5c0c9c-6a21-4c11-9680-9f5ebcdd3e45', passphrase='iliketurtles', is_sandbox=False, url='https://api.kucoin.com')

USDT_funds = int(exchange.fetch_balance().get('USDT').get('free'))
BTC_coins = float(exchange.fetch_balance().get('BTC').get('free'))

params1 = {
    'funds': int(exchange.fetch_balance().get('USDT').get('free'))
}

params2 = {
    'size': float(exchange.fetch_balance().get('BTC').get('free'))
}

def order(order_action):
    if order_action == 'buy':
        market_order = exchange.create_market_buy_order('BTC-USDT', USDT_funds)
    elif order_action == 'sell':
        market_order = exchange.create_market_sell_order('BTC-USDT', BTC_coins)
    return market_order


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Double Trio'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return 'success'
    elif request.method == 'POST':
        data = json.loads(request.data)
        if data['passphrase'] != "iliketurtles":
            return {
                "code": "error",
                "message": "invalid passphrase"
            }
        #if USDT_funds > 0:
            #buy_order = clientTrade.create_market_order('BTC-USDT', 'buy', funds=USDT_funds)
        #else:
            #sell_order = clientTrade.create_market_order('BTC-USDT', 'sell', size=BTC_coins)
        order(data['strategy']['order_action'])
        return "success"

#if __name__ == "__main__":
    #app.run(port=80)










