
from typing import List


def generate_list(l: List[int]) -> list:
    new_list = []
    for elem in l:
        new_list.append(str(elem))
    return new_list

list_sample = [1, 5, 8, 0, 12]
print(generate_list(list_sample))