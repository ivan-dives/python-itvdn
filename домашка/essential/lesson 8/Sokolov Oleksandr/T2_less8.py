import random
import pickle

lst = [random.randint(-100, 100) for x in range(1000)]

with open('Example.bin', 'wb') as f:
    pickle.dump(lst, f)

with open('Example.bin', 'rb') as f:
    lst_from_f = pickle.load(f)
    print(lst_from_f)
    f.close()
c = sum(lst)
print(c)