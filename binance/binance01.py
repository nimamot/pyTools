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
    trade_type = input("type( LIMIT(L) || MARKET(M) ): ")
    trade_action = input("BUY || SELL : ")
    trade_symbole = input("asset: (e.g: ETHUSDT): ")
    trade_amount = float(input("quantity: "))

    if (trade_action == "BUY"):
        if(trade_type == "LIMIT" or trade_type == "L"):
            trade_limit_price = float(input("specify limit order price: "))
            buy_order_limit = client.create_test_order(
            symbol='trade_symbole',
            side='BUY',
            type='LIMIT',
            timeInForce='GTC',
            quantity= trade_amount,
            price=trade_limit_price
            )

        elif(trade_type == "MARKET" or trade_type == "M"):
            buy_order = client.create_test_order(
            symbol= trade_symbole,
            side= 'BUY',
            type= 'MARKET',
            quantity= trade_amount)



    elif(trade_action == "SELL"):
        pass



print("-------------WELCOME----------------")
print("                                    ")
api_key = input("input your key: ")
api_secret = input("input your secret key: ")
client = Client(api_key, api_secret)

def main():
    action = input("what do you wanna do?(BALANCE(b) / PRICE(p) / OPENORDERS(oo)) / TRADE(T)")

    if action == "BALANCE" or action == "b":
        checkBalance()


    # getting the latest price
    elif action == "PRICE" or action == "p":
        checkPrice()


    elif action == "OPENORDERS" or action == "oo":
        openOrders()

    elif action == "TRADE" or action == "T":
        trade()


    else:
        print("wrong input")

while True:
    main()
