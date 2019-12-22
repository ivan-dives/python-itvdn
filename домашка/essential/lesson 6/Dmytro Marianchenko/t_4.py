param = {"Toyota": 25, "Mazda": 30, "Mitsubishi": 15}
print(param)
for key, values in param.items():
    print(key)
print()
for key, values in param.items():
    print(values)
print()
for key, values in param.items():
    print(f"{key} in stock {values} cars")

