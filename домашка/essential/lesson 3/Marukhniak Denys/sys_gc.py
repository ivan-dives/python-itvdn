# дополнительное задание для всей группы (для тех кто хочет хорошо разобраться в питоне) по счётчику ссылок:
# объясните действие

import sys
import gc

i = 'abcde'
q1 = sys.getrefcount(i)  # return the reference count for an object (plus one :-)
print(q1)
print(type(q1))
q2 = gc.get_referrers(i)  # Return the list of objects that refer to an object.
print(q2)
print(type(q2))
