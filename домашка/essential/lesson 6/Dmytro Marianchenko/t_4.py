def base(**kwargs):
    base_car = kwargs
    return base_car


param = {"Toyota": 25, "Mazda": 30, "Mitsubishi": 15}
base_res = base(**param)
print(*base_res)
print()
for key, values in base_res.items():
    print(key)
print()
for key, values in base_res.items():
    print(values)
print()
for key, values in base_res.items():
    print(f"{key} in stock {values} cars")

