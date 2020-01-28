import json

data1 = {"car1": "BMW", "car2": "Honda", "car3": "Lotus"}
data2 = {"car_color1": "white", "car_color2": "black", "car_color3": "yellow"}


with open("db.json", "w") as db:
    json.dump((data1, data2), db)


with open("db.json", "r") as db:
    load_data = json.load(db)

for i in load_data:
    print(f"\nloaded from 'db.json' = {type(i)} contain {i}")


load_data1 = load_data[0]
load_data2 = load_data[1]
print(f"\nDict 1 = {load_data1}\nDict 2 = {load_data2}")
