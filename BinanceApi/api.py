from binance.client import Client
import constants
client = Client(constants.API_KEY, constants.API_SECRET)

def get_eth_usdt_price():
    return client.get_symbol_ticker(symbol="ETHUSDT")['price']

def get_eth_balance():
    balances = client.get_account()['balances']
    for asset in balances:
        if asset['asset'] == 'ETH':
            return asset

def create_new_eth_order():
    return client.create_order(
    symbol='ETHUSDT',
    side='SELL',
    type='LIMIT',
    timeInForce='GTC',
    quantity=0.05,
    price=900)

print(get_eth_balance())
# print(create_new_eth_order())
print(client.get_open_orders())