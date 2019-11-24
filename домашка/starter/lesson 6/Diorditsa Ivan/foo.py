# def foo():
#     print("hi")
#     return
#
# def foo():
#     return print
#
# import functools
#
# def foo():
#     return functools.partial(print, "hi")
#
# foo()()

#######################

#def foo(x):
#    return x * x

#foo(2)
#foo(3)


# def fac(x):
#     if x == 1 or x == 0:
#         return 1
#     else:
#         result = fac(x-1)
#         result *= x
#         return result
#         # return x * fac(x-1)
#
# print(fac(4))

#################

# docstring

# def foo(x):
#     "это docstring"
#     return x * x
#
# print(help(foo))

########

# x = 0
#
# def foo():
#     x = 10
#
#     def bar():
#         nonlocal x
#         #x = 20
#         x = 10
#
#         print(x)
#
#     bar()
#     print(x)
#
# foo()

##################