import json

def get_price(name: str) -> int:
    with open('data/prices.json') as json_file:
        prices = json.load(json_file)
    price = prices[name]
    return price