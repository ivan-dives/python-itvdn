import math
func = input('Vvedite X' '\n' 'X = ')
func = float(func)
if -math.pi <= func <= math.pi:
    x = math.cos(3*func)
    print(x)
elif (-math.pi > func) or (math.pi < func):
    print(func)