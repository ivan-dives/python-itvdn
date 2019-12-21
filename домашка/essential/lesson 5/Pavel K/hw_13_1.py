def foo (z):
    return sum(z)/len(z)

z = tuple(map(int,input().split()))
print(foo(z))

______________________________

def foo(*args):
    return sum(args)/len(args)

y_nam = input('Enter your numbers: ')
y_nam = y_nam.split()
y_nam = [int(i) for i in y_nam]

print(foo(*y_nam))
