import random
import pickle


with open("some_text_b.dat", "wb") as f:
    lst = [random.uniform(1, 10000) for x in range(10000)]
    pickle.dump(lst, f)


with open("some_text_b.dat", "rb") as f:
    string = pickle.load(f)
    print(sum(string))
