ch1 = int(input('Число 1 = '))
ch2 = int(input("Число 2 = "))

def foo(x):
    if x == ch2:
        return (x)
    else:
        return foo(x+1)+x

print(foo(ch1))
