# Алгебраические выражения (x + y + z) и (x - y - z).
# Значения y и z вводяться с клавиатуры,
# функции positive() для x + y + z и negative() для x - y - z определяют результат
# данных выражений с плюсом и минусом соответственно при условии заданого значения x
# в диапазоне от -5 до 5 с шагом 0.5

y = float(input("value 1: "))
z = float(input("value 2: "))

def positive():
    x = -5.5
    while True:
        x += 0.5
        s = x + y + z
        if x > 5:
            break
        print(x,"=", s)

def negative():
    x = -5.5
    while True:
        x += 0.5
        s = x - y - z
        if x > 5:
            break
        print(x,"=", s)

print(positive())
print()
print(negative())