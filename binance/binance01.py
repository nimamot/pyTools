import os
from binance.client import Client



api_key = input("input your key:")
api_secret = input("input your secret key:")
client = Client(api_key, api_secret)
asset_input = input("asset:")
print(client.get_asset_balance(asset=asset_input))
