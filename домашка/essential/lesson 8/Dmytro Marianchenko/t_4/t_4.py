import json
import pickle
import ast
print("___________________________________________________")
print("ЗАПИСЫВАЮ В JSON ФАЙЛ:")
print()
products = {"Чайник": "1489 грн",
            "Утюг": "4299 грн",
            "Холодильник": "12999 грн"}
for key, values in products.items():
    print(f"{key} - {values}")  # выводим содержимое словаря
temp = pickle.dumps(products)  # cериализуем в "pickle"
var = {"temp": temp}  # присваеваем ключ и создаем словарь
with open("temp.json", "w") as file:
    json.dump(f"{var}", file)  # записываем в json
print("___________________________________________________")
print("ОТКРЫВАЕМ JSON ФАЙЛ:")
print()
with open("temp.json", "r") as f:
    var1 = json.load(f)  # принимаем данные из json
    dc = ast.literal_eval(var1)  # конвертим строку в ссловарь
    temp = dc.get("temp")  # принимаем данные по ключу
    products = pickle.loads(temp)  # распаковываем pickle
for key, values in products.items():
    print(f"{key} - {values}")
