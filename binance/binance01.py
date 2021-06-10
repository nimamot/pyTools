import os
from binance.client import Client

def checkBalance():
    asset_input = input("asset: ")
    asset_balance = client.get_asset_balance(asset=asset_input)

    for key, value in asset_balance.items():
        print(key, ':', value)
    print("-----------------------------")

def checkPrice():
    asset_input = input("Symbol(eg: ADAUST): ")
    asset_price = client.get_symbol_ticker(symbol=asset_input)
    for key, value in asset_price.items():
        print(key, ':', value)
    print("-----------------------------")

def openOrders():
    asset_input = input("Symbol(eg: ADAUST): ")
    openorders = str(client.get_open_orders(symbol= asset_input))
    values = openorders.split(",")
    for value in values:
        print(value)
    print("-----------------------------")


def trade():
    trade_asset = input("asset: ")
    trade_action = input("BUY | SELL : ")
    trade_amount = int(input("amount: "))


print("-------------WELCOME----------------")
print("                                    ")
api_key = input("input your key: ")
api_secret = input("input your secret key: ")
client = Client(api_key, api_secret)

def main():
    action = input("what do you wanna do?(BALANCE(b) / PRICE(p) / OPENORDERS(oo))")

    if action == "BALANCE" or action == "b":
        checkBalance()


    # getting the latest price
    elif action == "PRICE" or action == "p":
        checkPrice()


    elif action == "OPENORDERS" or action == "oo":
        openOrders()


    else:
        print("wrong input")

while True:
    main()
