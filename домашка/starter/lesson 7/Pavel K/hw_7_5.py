# мемоизация под факториал(7.5) (или фибоначчи(7.2) или любой другой алгоритм рекурсивный)
mim =[]
def fact(n):
    if n == 0:
        return 1
    else:
        if len(mim) > n:
            return mim[n]
        else:
            sumf = fact(n-1)*n
            mim.insert(0, sumf)
            return sumf


a = fact(int(input('факториал скольки ты хочешь увидеть ')))
print(a)
print(mim[::-1])