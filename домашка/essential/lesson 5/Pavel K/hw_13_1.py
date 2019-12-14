def foo (z):
    return sum(z)/len(z)

z = tuple(map(int,input().split()))
print(foo(z))