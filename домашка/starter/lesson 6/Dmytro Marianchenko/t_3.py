
def stear(steps):
   if steps == 0:
       return 0
   elif steps == 1:
       return 1
   else:
       return stear(steps-1) + stear(steps-2)

steps = int(input("Введите количество ступенек:  "))
print(f"Вы можете поднятся на {steps} ступенек, {stear(steps)} возможными вариантами")