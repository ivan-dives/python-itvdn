# import os
#
# os.path.isdir()

##################

x = 10
y = "строка"
z = 1.0

def z1():
    print("hello! I am function z1")


name = [10, "строка", 1.0, z1]

#print(name)

#name[3]()

#for o in name:
#    print(f'Hello, I am {type(o)}: {o}')

#for c in range(4):
#    print(f"hello, I am cell number {c}: {type(name[c])}: {name[c]}")

#print(name[0])


# empty = []
# #empty = list()
#
# while True:
#     x = input('введите число (или exit): ')
#     if x == 'exit':
#         break
#     else:
#         #empty.append(x)
#         empty.insert(0, x)
#
# print(f'считали следующие числа {empty}')


##################

# x = list(range(10))
# print(x)
# a = x.pop()
# print(a, x)
# a = x.pop(5)
# print(x)
# del x[3]
# print(x)

#####################

# x = 10
# print(id(x))
# x += 10
# print(id(x))
# y = 10
# print(id(y))
# x = 'string'
# print(id(x))

##################

# def foo(l):
#     l.append(20)
#
# L1 = []
# foo(L1)
# print(L1)

# x = 10
# y = 10
# print(id(x))
# print(id(y))

#a = []
#b = []
#print(id(a))
#print(id(b))

#print(a == b)
#print(a is b)
#if a:
#    print('true')

# s = "мама мыла раму"
# print(len(s))
#
# l = [ 10, 20 ,30]
# print(len(l))
# l.pop()
# print(len(l))
# l.append(55)
# print(len(l))

###################

# l = [10, 20, 30, 40]
# print(l.index(30))
# l.reverse()
# print(l)

###############

# l = [10, 20]
#
# a, b = l
# print(a)
# print(b)
#
# L1 = [a, b]
# print(L1)

# def foo():
#     return [10, 20, 30]
#
# l = foo()
# print(l)
# a, b, c = foo()
# print(a)
# print(b)
# print(c)
#x, z = foo()
#print(x)
#print(z)

#######################

# def foo(*args):
#     print(type(args))
#     print(args)
#     #args.append(200)
#
# foo(10, 20)

##########################

#l = [ 10, 20, 30]
#print(*l)

#a, *b = [10]
#print(a, b)

############################

# l = list(range(5))
# print(l)
# print(l[0:3:2])
# print(l[::-1])
# print(l[2:])
# print(l[:3])

########################

# l = [10, 'str', [10, 20]]
#
# tmp = l[2]
# print(tmp[1])
#
# print(l[2][1])

#########################

# list comprehension

# l = [10, 'str', 1.0]
# print(l)
# l2 = [type(x) for x in l]
# print(l2)

# s = '10,20,30'
# print(s.split(','))
# l = [int(x) for x in s.split(',')]
# print(l)

#l = [10, 20, 30]
#print([x*x for x in l])

#s = '10 20 exit 30'
#print([int(x) for x in s.split() if x.isdigit()])


# >>> [a if a else 2 for a in [0,1,0,3]]

#print([int(x) if x.isdigit() else x.upper() for x in s.split()])

#x = [10, 20, 30]
#y = x
#import copy
#y = copy.deepcopy(x)
#print(id(x), id(y))

#y = x[::]
#print(id(x), id(y))

#x = [ 1, 2, 3]

#print(x[-100])

# OPERATIONS = ['+', '-', '/', '*']
#
# op = '+'
#
# if op in OPERATIONS:
#     print('да')

##################

# a = [10, 20]
# b = [30, 40]
#
# print(b + a)

# x = [10, 20, 30]
#
# #x[0:2] = [5,6]
# x.extend([100,200,400])
# print(x)



# Числа Фибоначчи

# # Количество чисел в последовательности
# n = 10
# # Список чисел Фибоначчи (изначально - две единицы)
# fibs = [1, 1]
#
# # Повторяем n - 2 раз, так как два числа уже в списке
# for i in range(n - 2):
#     # Добавляем сумму двух последних чисел
#     fibs.append(fibs[i] + fibs[i + 1])
#
# # Вывод списка на экран
# print(fibs)

#############################



