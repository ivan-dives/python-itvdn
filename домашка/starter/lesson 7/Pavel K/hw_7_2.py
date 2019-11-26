mim = [0,1,2]
def fib(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        if len(mim) > n:
            return mim[n]
        else:
            sumf = fib(n - 1) + fib(n - 2)
            mim.insert(n,sumf)
            return sumf

print(fib(int(input('put number Fibonacci'))))
print(mim)