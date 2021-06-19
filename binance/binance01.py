import os
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException

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
        # MARKET LIMIT ORDER
        if(trade_type == "LIMIT" or trade_type == "L"):

            try:
                trade_limit_price = float(input("specify limit order price: "))
                # to make a real order remove "_test"
                buy_order_limit = client.create_test_order(
                symbol=trade_symbole,
                side='BUY',
                type='LIMIT',
                timeInForce='GTC',
                quantity= trade_amount,
                price=trade_limit_price
                )
                print(buy_order_limit)

            except BinanceAPIException as e:
                # error handling goes here
                print("Binance API Exception Error")
            except BinanceOrderException as e:
                # error handling goes here
                print("Binance Order Exception Error")

        # MARKET BUY ORDER
        elif(trade_type == "MARKET" or trade_type == "M"):
            try:
                # to make a real order remove "_test"
                buy_order = client.create_test_order(
                symbol= trade_symbole,
                side= 'BUY',
                type= 'MARKET',
                quantity= trade_amount)
                print(buy_order)

            except BinanceAPIException as e:
                # error handling goes here
                print("Binance API Exception Error")
            except BinanceOrderException as e:
                # error handling goes here
                print("Binance Order Exception Error")



    elif(trade_action == "SELL"):

        try:
            # to make a real order remove "_test"
            trade_limit_price = float(input("specify limit order price: "))
            sell_order_limit = client.create_test_order(
            symbol=trade_symbole,
            side='SELL',
            type='LIMIT',
            timeInForce='GTC',
            quantity= trade_amount,
            price=trade_limit_price
            )

            for key, value in sell_order_limit.items():
                print(key, ':', value)
            print("order confirmed!")
            print("-----------------------------")


        except BinanceAPIException as e:
            # error handling goes here
            print("Binance API Exception Error")
        except BinanceOrderException as e:
            # error handling goes here
            print("Binance Order Exception Error")


# MARKET BUY ORDER
    elif(trade_type == "MARKET" or trade_type == "M"):
        try:
            # to make a real order remove "_test"
            sell_order = client.create_test_order(
            symbol= trade_symbole,
            side= 'SELL',
            type= 'MARKET',
            quantity= trade_amount)
            print(sell_order)

        except BinanceAPIException as e:
            # error handling goes here
            print("Binance API Exception Error")
        except BinanceOrderException as e:
            # error handling goes here
            print("Binance Order Exception Error")




print("-------------WELCOME----------------")
print("                                    ")
print("                                    ")
api_key = input("input your key: ")
api_secret = input("input your secret key: ")
print("user verified")
client = Client(api_key, api_secret)

def main():
    action = input("what do you wanna do? \n 1) Check your balace for an asset: BALANCE(b) \n 2) Check the price for an asset: PRICE(p) \n 3) Check your open Orders: OPENORDERS(oo) \n 4) trade: TRADE(T) \n")

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
