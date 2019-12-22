import os
import csv

print(f'\nLocation for searching config.txt:\n{os.getcwd()}...')
if 'config.txt' in os.listdir(os.getcwd()):
    print('config.txt has found\n')
else:
    print('config.txt has not found\n')
    exit()

with open('config.txt') as f:
    config = f.read()

print('Information in config.txt:')
print(config)

dict_config = {}
tmp = config.split()
print()
for x in tmp:
    split_tmp = x.split(sep='=')
    up_tmp = {split_tmp[0]: split_tmp[1]}
    dict_config.update(up_tmp)
print(f'Config into dict:\n{dict_config}\n')

print('Printed dict:')
for key, values in dict_config.items():
    print(f'{key} = {values}')
print(dict_config.get('age', 'Form "Age" has not found\n'))

dict_config.update({'username': 'petr'})
# pas_new = input('Enter new password: ')
dict_config.update({'password': 'pas_new'})

print('Changed dict: ')
for key, values in dict_config.items():
    print(f'{key} = {values}')

print('\nChanged dict into string:')
print(dict_config)
list_tmp = []
string = ''
for key, values in dict_config.items():
    str_tmp = f'{key}={values}'
    list_tmp.append(str_tmp)

str_sep = '\n'
string += str_sep.join(list_tmp)

print(string)
with open('config.txt', 'w') as f:
    f.write(string)


# csv
def csv_writer(csv_data, csv_path):
    with open(csv_path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in csv_data:
            writer.writerow(line)


print('\nChanged dict into cvs_data:')
print(dict_config)
data = [[], []]
for key, values in dict_config.items():
    data[0].append(key)
    data[1].append(values)
print(data)
w_path = "config.csv"
csv_writer(data, w_path)


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))


print('\nRead config.csv')
r_path = "config.csv"
with open(r_path, "r") as f_obj:
    csv_reader(f_obj)
