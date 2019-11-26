
def natural1(num1):
    if num1 == num2:
        return num2
    else:
        return num1+natural1(num1-1)

def natural2(num2):
    if num2 == num1:
        return num1
    else:
        return num2+natural2(num2-1)

print()
num1 = int(input("Введи число от которого начнем вычислять сумму натуральных чисел:  "))
num2 = int(input("Введи число до которого будем высчитывать сумму натуральных чисел:  "))
if num1 < num2:
    print()
    print(f"Отлично, считаем сумму натуральных чисел от {num1} до {num2}")
    print(f"Сумма диапазона введенных тобой натуральных чисел равна {natural2(num2)}")
else:
    print()
    print(f"Отлично, считаем сумму натуральных чисел в обратном порядке от {num1} до {num2}")
    print(f"Сумма диапазона введенных тобой натуральных чисел равна {natural1(num1)}")