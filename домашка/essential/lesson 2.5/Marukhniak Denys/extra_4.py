class Decorator:

    def __init__(self, function):
        self.function = function

    def __call__(self, num):
        if isinstance(self.function(num), int):
            return self.function(num)


@Decorator
def factorial(f):
    if len(memoize) > f:
        return memoize[f]
    else:
        memoize.append(memoize[len(memoize)-1]*len(memoize))
        return factorial(f)


@Decorator
def fib(s):
    if len(memoize_f) > s:
        return memoize_f[s]
    else:
        memoize_f.append(memoize_f[len(memoize_f)-1]+memoize_f[len(memoize_f)-2])
        return fib(s)


memoize_f = [0, 1, 2, 3]
memoize = [1, 1]

print(f'Factorial {5}! = {factorial(5)}')
print(f'Fibonacci: {fib(5)}')
