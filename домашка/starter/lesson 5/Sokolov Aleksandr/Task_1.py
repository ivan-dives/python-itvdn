name = input('Your name is: ')
def baz():
     if name == '':
         print('Hello, ', 'Aleks', '!', sep='')
     else:
         print('Hello, ', name, '!', sep='')

baz()