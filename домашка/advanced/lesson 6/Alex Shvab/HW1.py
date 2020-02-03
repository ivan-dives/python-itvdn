from typing import List


def foo(some_value: List[int]) -> List[str]:
    res = []
    for i in some_value:
        temp = str(i)
        res.append(temp)
    return res

foo([1, 2, 3])
foo([1,3, "lol"])