# Задание
# Напишите рекурсивную функцию, которая вычисляет сумму натуральных чисел, которые
# входят в заданный промежуток.


def foo(a, b, res):
    res += a
    a += 1
    if a <= b:
        return foo(a, b, res)
    else:
        return res


# a = int(input('From '))
# b = int(input('to '))
a = 3
b = 5
print(foo(a, b, res=0))
