import json

dictionary = {'ip_1': '192.168.0.0',
              'ip_2': '192.168.0.1',
              'ip_3': '192.168.0.2',
              'ip_4': '192.168.0.3'}
with open('myfile.json', 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(dictionary, indent=2, ensure_ascii=False))

input("enter")

path = 'myfile.json'
with open(path, 'r', encoding='utf-8') as foo:
    myfile = json.load(foo)

print(myfile)
