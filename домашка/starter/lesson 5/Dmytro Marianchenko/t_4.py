def arif(a,b,c):
    sum = (a+b+c)/3
    print(round(sum,2))

print("""
    Введи три числа для определения среднего арифметического значения
    """)
a = int(input("Введи первое число:  "))
print(f"Первое число '{a}'")
b = int(input("Введи второе число:  "))
print(f"Пеервое число '{a}', второе число '{b}'")
c = int(input("И еще одно число:  "))
print(f"Пеервое число '{a}', второе число '{b}', третье число '{c}'")
print()
print("Среднее арифметическое твоих чисел равняется:")
arif(a,b,c)