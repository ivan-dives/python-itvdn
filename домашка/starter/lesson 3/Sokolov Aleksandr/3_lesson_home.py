#Lesson3

#Task1
name = input("What's your name? ")
if name == "Aleks":
    print("Have a nice day, {0}".format(name))

#Taks_2
import math
x = int(input('number: '))
if -math.pi <= x <= math.pi:
    y = math.cos(3*x)
elif x < -math.pi or x > math.pi:
    y = x
print(y)

#Task_3
import math
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
d = (b**2) - (4*a*c)
if d < 0:
    print('There no real math roots')
elif d == 0:
    x = -b/(2*a)
    print(x)
else:
    x_1 = (-b-math.sqrt(d))/(2*a)
    x_2 = (-b+math.sqrt(d))/(2*a)
    print('Solution are {0} and {1}'.format(x_1,x_2))


#Additional task
# С функциями sin, cos, tan работает не правильно, если вводить число, а потом функцию sin, cos, нужно еще третье число ввести, чтобы вывести результ
#Как калькулятор правильнее было бы написать или оптимизировать?
print('Calculator')
a = int(input('number: '))
b = input('select operation ')
c = int(input('number: '))
import math
if b == 'sin':
    print('result:', math.sin(a))
elif b == 'cos':
    print('result:', math.cos(a))
elif b == 'tan':
    print('result:', math.tan(a))
if b == '+':
    print('result:', a+c)
elif b == '-':
    print('result:', a-c)
elif b == '*':
    print('result:', a*c)
elif b == '/':
    print('result:', a/c)
elif b == '**':
    print('result:', a**c)


