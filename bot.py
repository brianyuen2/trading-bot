from api import *

# Main logic function, pulls information from account and exchange before
# deciding to trade or not
def attempt_trade():
    # if certain indicators are __ 
    balance = get_eth_usdt_balance()
    create_new_eth_order('SELL', 0.1)
    print('trade')

# Bot loop cycle
# attempts to make a trade every 30 sec
def run_bot():
    while(1):
        attempt_trade()
        time.sleep(30)

run_bot()