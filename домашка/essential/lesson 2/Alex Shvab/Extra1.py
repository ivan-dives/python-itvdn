import  time

fib_list = [1, 2]
fac_list = []

def timer(f):

    def tmp(n):
        start = time.time()
        f(n)
        end = time.time()
        timer = (end - start) * 1000
        print(f"Time: {timer} milliseconds")
    return  tmp


@timer
def fib(x):
    for i in range (x - 2):
        fib_list.append(fib_list[i] + fib_list[i+1])

@timer
def factorial(x):
    res = 1
    if x >= 1:
        for i in range(1, x + 1):
            res = res * i
            fac_list.append(res)


n = int(input("Enter a number: "))
print("Fibonacci")
fib(n)
print(fib_list)
print()
print("Factorial")
factorial(n)
print(fac_list)