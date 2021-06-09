import os
from binance.client import Client


print("-------------WELCOME----------------")
print("                                    ")
api_key = input("input your key: ")
api_secret = input("input your secret key: ")
client = Client(api_key, api_secret)

action = input("what do you wanna do?(BALANCE / PRICE / OPENORDERS)")



def checkBalance():
    asset_input = input("asset: ")
    print(client.get_asset_balance(asset=asset_input))

def checkPrice():
    asset_input = input("Symbol(eg: ADAUST): ")
    asset_price = client.get_symbol_ticker(symbol=asset_input)
    print(asset_price)


def openOrders():
    asset_input = input("Symbol(eg: ADAUST): ")
    openorders = str(client.get_open_orders(symbol= asset_input))
    print(openorders)
    values = openorders.split(",")
    for value in values:
        print(value)





if action == "BALANCE":
    checkBalance()

# getting the latest price
elif action == "PRICE":
    checkPrice()

elif action == "OPENORDERS" or action == "oo":
    openOrders()

else:
    print("wrong input")
