from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException
import constants
import time
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s',
 datefmt='%d-%b-%y %H:%M:%S')

client = Client(constants.API_KEY, constants.API_SECRET)

# Returns eth/usdt current price
def get_eth_usdt_price():
    try:
        return client.get_symbol_ticker(symbol="ETHUSDT")['price']
    except:
        logging.error('Error getting price')

# Returns eth and usdt balances for the account in an array
def get_eth_usdt_balance():
    try:
        balances = client.get_account()['balances']
        assets = []
        for asset in balances:
            if asset['asset'] == 'ETH' or asset['asset'] == 'USDT':
                assets.append(asset)
        return assets
    except:
        logging.error('Error getting balances')

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
        price=900
    )
    except BinanceAPIException as e:
        # error handling goes here
        logging.error(e)
    except BinanceOrderException as e:
        # error handling goes here
        logging.error(e)

# create_new_eth_order('SELL', 0.1)