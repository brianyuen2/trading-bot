from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException
import constants
import time

client = Client(constants.API_KEY, constants.API_SECRET)

# Returns eth/usdt current price
def get_eth_usdt_price():
    try:
        return client.get_symbol_ticker(symbol="ETHUSDT")['price']
    except:
        print('Error getting price')

# Returns eth and usdt balances for the account in an array
def get_eth_usdt_balance():
    balances = client.get_account()['balances']
    assets = []
    for asset in balances:
        if asset['asset'] == 'ETH' or asset['asset'] == 'USDT':
            assets.append(asset)
    return assets

# Creates a new order for eth/usdt
# takes in side and quantity
def create_new_eth_order(side, quantity):
    # Remove test when real trades are wanted
    try:
        return client.create_test_order (
        symbol='ETHUSDT',
        side=side,
        type='MARKET',
        quantity=quantity,
    )
    except BinanceAPIException as e:
        # error handling goes here
        print(e)
    except BinanceOrderException as e:
        # error handling goes here
        print(e)

# run_bot()
# create_new_eth_order('SELL', 0.1)