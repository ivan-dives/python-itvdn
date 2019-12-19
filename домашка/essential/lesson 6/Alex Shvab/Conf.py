dic = {}
with open('config.txt') as f:
    config = f.read()

#print(config)

lst = config.split()
for i in lst:
    split_lst = i.split("=")
    dic[split_lst[0]] = split_lst[1]

for key, value in dic.items():
    print(key, value)

print()

print(dic.get("age", "Sorry incorrect request"))
dic["username"] = "petr"
dic["password"] = "He11o"

print()

for key, value in dic.items():
    print(key, value)

res = ""
for key, value in dic.items():
    res += f"{key} = {value}\n"

print()
print(res)

with open('config.txt', 'w') as f:
    f.write(res)

#print(dic)