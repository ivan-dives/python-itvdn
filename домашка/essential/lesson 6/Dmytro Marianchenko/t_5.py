with open('conf.txt') as f:
    config = f.read()


def prt(config_dict):
    for key, values in config_dict.items():
        print(f"{key} = {values}")


def lst(config_dict):
    var = []
    lst_encode = []
    for key, values in config_dict.items():
        x = key
        y = values
        var.append(x)
        var.append(y)
        lst_encode.append(var)
    return lst_encode[0]


config = config.replace("=", "\n")
container = config.split("\n")
config_dict = {container[i]: container[i + 1] for i in range(0, len(container), 2)}
print()
print("  <<  read data from 'conf.txt' >>  ")
print()
prt(config_dict)
print()
print("  <<  changing data to >>  ")
print()
config_dict.update({"username": "petr", "password": "new_password"})
config_dict["age"] = "33"
prt(config_dict)
print()
lst_data = lst(config_dict)
string = " ".join(lst_data)

print("  <<  writing data as 'string' to 'conf.txt'  >>  ")
with open('conf.txt', 'w') as f:
    f.write(string)
