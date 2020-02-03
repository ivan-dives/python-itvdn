import typing

T = typing.TypeVar('T')


#print(type(typing.TypeVar))


def foo(n: T) -> T:
    return n


x = 20
x += foo(10)
y = 'abc'
y *= foo('строка')

exit()

class Car:
    MAXIMUM_SPEED: typing.ClassVar[int] = 100

car = Car()
car.MAXIMUM_SPEED = 20

exit()


def divide(x: typing.Union[int, float], y) -> typing.Union[float, None]:
    try:
        return x / y
    except ZeroDivisionError:
        return None


print(divide(10, 2))
#print(divide(10, 0))
x = divide(10, 0)
print(x / 10)
divide("строка", 10)

exit()

def bar(x: int):
    return x * x

#def foo():
#    s = input()

#x = foo()
#x += 2

print(bar(2))
#print(bar("строка"))
