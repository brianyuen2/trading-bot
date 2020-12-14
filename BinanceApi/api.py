from binance.client import Client
import constants
client = Client(constants.API_KEY, constants.API_SECRET)


# print(client.get_symbol_info('ETHUSDT'))
price = client.get_symbol_ticker(symbol="ETHUSDT")
print('Price for ETH/USDT is: ' + price['price'])