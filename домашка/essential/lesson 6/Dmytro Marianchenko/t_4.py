def base(**kwargs):
    base_car = kwargs
    return base_car


param = {"Toyota": 25, "Mazda": 30, "Mitsubishi": 15}
base_res = base(**param)
print(base_res)

