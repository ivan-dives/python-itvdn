from timeit import default_timer as timer


def time_of_work(f):
    start = timer()

    def time(number):
        if isinstance(f(number), int):
            print(f'Result: {f(number)}')
        else:
            end = timer()
            time_of_operation = (end - start)
            return f'Time of operation {time_of_operation} seconds'
    return time


@time_of_work
def factorial(f):
    if len(memoize) > f:
        return memoize[f]
    else:
        memoize.append(memoize[len(memoize)-1]*len(memoize))
        return factorial(f)


@time_of_work
def fib(s):
    if len(memoize_f) > s:
        return memoize_f[s]
    else:
        memoize_f.append(memoize_f[len(memoize_f)-1]+memoize_f[len(memoize_f)-2])
        return fib(s)


memoize_f = [0, 1, 2, 3]
memoize = [1, 1]

print(f'Factorial: {5}!')
print(factorial(5))
print()
print(f'Fibonacci:')
print(fib(5))
