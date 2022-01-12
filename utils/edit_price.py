import json

def edit_price(name: str, price: int):
    with open('data/prices.json', 'r') as json_file:
        config = json.load(json_file)
        config[name] = price

    with open('data/prices.json', 'w') as json_file:
        json.dump(config, json_file)