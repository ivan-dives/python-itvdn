class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

print(A.__mro__) # (<class '__main__.A'>, <class 'object'>)
print(B.__mro__) # (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
print(C.__mro__) # (<class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.__mro__) # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)