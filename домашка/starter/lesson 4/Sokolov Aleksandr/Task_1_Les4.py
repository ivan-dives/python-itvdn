a, b = map(int, input().split())
if a < b:
    oper = 0
    for i in range(a, b+1):
        oper += i
        print(oper)
else:
    print('The condition is not fulfilled')