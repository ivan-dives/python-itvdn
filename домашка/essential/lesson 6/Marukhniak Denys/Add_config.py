import os

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
print(f'Config into dict:\n{dict_config}')

print('\nPrinted dict:')
for key, values in dict_config.items():
    print(f'{key} = {values}')
print(dict_config.get('age', 'Form "Age" has not found\n'))

dict_config.update({'username': 'petr'})
# pas_new = input('Enter new password: ')
dict_config.update({'password': 'pas_new'})

print('\nChanged dict: ')
for key, values in dict_config.items():
    print(f'{key} = {values}')

print('\nChanged dict into string:')
print(f'{dict_config}')
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

# import pathlib
# print(os.listdir(os.getcwd()))
# PATH = pathlib.Path(os.getcwd()) / '..'
# print(PATH)
# print(os.listdir(PATH))
# os.chdir(PATH)
# print(os.getcwd())
# print(os.listdir(os.getcwd()))
# print(PATH)
# print(os.listdir(PATH))
