# Прочитайте в документации по языку Python информацию о перечисленных в резюме данного
# урока стандартных функциях. Проверьте их на практике.

#  Зададим значения переменным
a = 10
b = 22
c = 13
d = "t"
e = "Aqlafoiasdhf"
f = "abba"

# Проверим некоторые функции
help(print())

print(bin(a))
print(bool(a))
print(chr(b))
print(float(a))

print(hex(a))
print(id(a))
print(len(e))
print(max(a, b, c))
print(min(a, b, c))
print(oct(a))
print(ord(d))
print(sorted(e))
print("".join(sorted(e)))
print(f)
print("".join(reversed(f)))
print(f[::-1])