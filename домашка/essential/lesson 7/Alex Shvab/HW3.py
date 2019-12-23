import sys
import os
import pathlib
p = pathlib.Path(os.getcwd())
p /= "../../../starter/lesson 7/Alex Shvab"
p = p.resolve()

sys.path.insert(0, str(p))


import HW3

x = int(input("Enter range of simple number: "))
HW3.simpl_numb(x+1)
print((HW3.list))