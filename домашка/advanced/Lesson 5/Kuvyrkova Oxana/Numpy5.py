import numpy as np
from itertools import chain

temperature = np.random.randint(15, 31, 90)
print(temperature)

np.save('data.npy', temperature)
new_arr = np.load('data.npy').reshape((-1,2))

print(new_arr)
print(f"min = {new_arr.min()}, max = {new_arr.max()}, aver = {new_arr.mean()}")
arr_month = new_arr.reshape((3,30))
print(arr_month)

last_5 = arr_month[:3, -6:]
print(last_5)
np.savetxt('last_5.txt', last_5)
