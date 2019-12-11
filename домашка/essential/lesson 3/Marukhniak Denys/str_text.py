# объясни как count - метод класса который должен принимать два параметра
# self и sub, уходит в max, где ему передаётся только один аргумент sub
# другими словами, https://docs.python.org/3/library/stdtypes.html?highlight=count#str.count
# str.count(sub[, start[, end]])

# это метод класса, т.е. ты не можешь его вызвать как
# str.count('a'), потому что нужен self

print('------------------------------------')
text = 'dfsdf'
print(type(text))
print('------------------------------------')
x = str.count
print(x)
print(type(x).__mro__)
# объясни почему я не могу сделать x('a')
print(type(str.count(text, 'a')))
print(str.count(text, 'a'))
# но могу сделать c('a')
print('------------------------------------')
c = text.count
print(c)
print(type(c).__mro__)
print(type(c('a')))
print(c('a'))  # print(text.count('a'))
print('------------------------------------')
# zxc = '{}asd'
# v = zxc.format
# print(v(123))
print('{}dsa'.format(321))
print(str.format('{}dsa', 321))
print('------------------------------------')
# cxz = 321
# b = cxz.bit_length
# print(b())
print((321).bit_length())
print(int.bit_length(321))
print('------------------------------------')


class A:
    def __init__(self, name):
        self.name = name

    def change(self):
        self.name = 11
        return self.name


z = A(135)
print(A.change(z))
print(z.change())
