import math
print("Введите значение 'x':")
x = int(input(""))
if -math.pi <= x <=math.pi:
    y = math.cos(3*x)
    print(f"Ответ: {y}")
elif x < -math.pi or x > math.pi:
    y = x
    print(f"Ответ: {y}")
input("Для завершения нажмите 'Enter'...")