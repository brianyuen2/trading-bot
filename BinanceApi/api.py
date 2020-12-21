from binance.client import Client
import constants
import time

client = Client(constants.API_KEY, constants.API_SECRET)

# Returns eth/usdt current price
def get_eth_usdt_price():
    return client.get_symbol_ticker(symbol="ETHUSDT")['price']

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
    return client.create_test_order(
    symbol='ETHUSDT',
    side=side,
    type='MARKET',
    quantity=quantity,
)

# Main logic function, pulls information from account and exchange before
# deciding to trade or not
def attempt_trade():
    # if certain indicators are __ 
    balance = get_eth_usdt_balance()
    print(balance)

# Bot loop cycle
# attempts to make a trade every 30 sec
def run_bot():
    while(1):
        attempt_trade()
        time.sleep(30)


run_bot()
# create_new_eth_order('SELL', 0.1)