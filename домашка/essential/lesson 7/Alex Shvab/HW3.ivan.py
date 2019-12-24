#from HW3 import *

import sys
import os
#print(os.getcwd())
#import os.path
#p = os.path(os.getcwd() + '')
import pathlib

p = pathlib.Path(os.getcwd())
p /= '../../../starter/lesson 7/Alex Shvab'
p = p.resolve() # print(p.resolve())
print(p)
sys.path.insert(0, str(p))
print(sys.path)
#sys.path.insert(0, '/starter/lesson7/Alex Shvab/')
#sys.path.insert(0, '/home/ivan/PycharmProjects/python-itvdn/домашка/starter/lesson 7/Alex Shvab')
import HW3
#import pprint
#pprint.pprint(sys.modules)

x = int(input("Enter count of simple number: "))
HW3.simpl_numb(x+1)
print((HW3.list))