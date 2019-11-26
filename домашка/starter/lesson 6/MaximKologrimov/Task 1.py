# Задание 1
# Прочитайте в документации по языку Python информацию о перечисленных в резюме данного
# урока стандартных функциях. Проверьте их на практике.

def foo(a):
    """
    Задание 1
    Прочитайте в документации по языку Python информацию о перечисленных в резюме данного
    урока стандартных функциях. Проверьте их на практике.
    """
    a += 1
    return a

x = 5
y = -5
real = -7
imag = 7
z = 7.1234567
s = 'Abraham'

print('abs(x) =', abs(x))
print('bin(x) =', bin(x))
print('bool(x) =', bool(x))
print('callable(f) =', callable(foo), callable(x))
print('chr(code) =', chr(1052))
print('complex(real, imag) =', complex(real, imag))
print('dir(obj) =', dir(print))
print('float(x) =', float(x))
print('format(x, fmt) =', '{}, {}'.format(y, x))
print('help(obj) =', help(print))
print('hex(x) =', hex(x))
print('id(obj) =', id(foo))
#input('who are you?')
print('int(x) =', int(x))
print('len(s)', len(s))
print('max(arg1, arg2, …) =', max(2, 77, 10))
print('min(arg1, arg2, …) =', min(2, 77, 10))
print('oct(x) =', oct(x))
print('ord(c) =', ord('m'))
print('pow(x, n) =', pow(x, imag))
print('print()')
print('range() =', min(range(77)),',', max(range(77)))
print('repr(obj) =', repr(help))
print('reversed(iterable):', list(reversed(s)))
for i in reversed(range(7)):
    print(i)
print('round(number, ndigits) =', round(z,2))
print('sorted(iterable) =', sorted(s))
print('str(x) =', type(str(x)), type(x))
print(foo.__doc__)
