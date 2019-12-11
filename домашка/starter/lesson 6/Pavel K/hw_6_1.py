def foo():
    print('1')


a, b = 5, 10
c = 'string'

###############################################################

print(abs(-5))  # 5
print(bin(5))  # 0b101
print(bool(' '))  # True
print(callable(foo), callable(print))  # True True
print(chr(78))  # N
print(complex(-4 ** 0.5))  # (-2+0j)
print(dir(help))  # ['__call__', '__class__', '__delattr__', ... ]
print(float(1))  # 1.0
print('первое {} второе {}'.format(a, b))  # первое 5 второе 10
# print(help(help())) # Welcome to Python 3.7's help utility! ...
print(hex(15))  # 0xf
print(id(a))  # 1549690096
# print(input('input and then i print')) # 56
print(int('5'), int(3.9))  # 5 3
print(len(c))  # 6
print(max(range(10, 99999)))  # 99998
print(min(range(10, 99999)))  # 10
print(oct(8))  # 0o10
print(ord('c'))  # 99
print(pow(0, 0))  # 1
print('4 + 53', 3 + 45)  # 4 + 53    48
print(list(range(5)), range(5))  # [0, 1, 2, 3, 4] range(0, 5)
print(repr(c))  # 'string'
print(list(reversed(c)))  # ['g', 'n', 'i', 'r', 't', 's']
print(round(454543534.4343434, -4)) # 454540000.0
print(sorted(c)) # ['g', 'i', 'n', 'r', 's', 't']
print(type(a),type(str(a))) # <class 'int'> <class 'str'>