import json
import pickle

products = [
    {"Apple" : 8},
    {"Books" : 10},
    {"Cheese" : 20},
    {"Bread" : 15}
]

print("Json")
with open("json.txt", "w") as file:
    json.dump(products, file)

with open("json.txt", "r") as file:
    staff = json.load(file)
print(staff)

print("Pickle")
with open("pickle.txt", "wb") as file:
    pickle.dump(products, file)

with open("pickle.txt", "rb") as file:
    staff = pickle.load(file)
print(staff)

