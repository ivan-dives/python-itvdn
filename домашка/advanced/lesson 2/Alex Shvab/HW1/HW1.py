import json

products = [
    {"Apple": 8},
    {"Books": 10},
    {"Cheese": 20},
    {"Bread": 15},
    {"Pork": [2, 4, 7]}
]

with open("shop.json", "w") as file:
    json.dump(products, file)

with open("shop.json", "r") as file:
    data = json.load(file)
    print(data)
