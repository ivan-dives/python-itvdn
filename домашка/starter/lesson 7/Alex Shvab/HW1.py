def min(list):
    res = list[0]
    for x in list:
        if x < res:
            res = x
    return res

def max(list):
    res = list[0]
    for x in list:
        if x > res:
            res = x
    return res

def sum(list):
    res = 0
    for x in list:
        res += x
    return res

def avg(list):
    res = 0
    for x in list:
        res += x
    res = res / len(list)
    return res

list = [1, 200, 0, 4, 5, -1, 7, 8, 20, 10]
print(f"Min element = {min(list)}")
print(f"Max element = {max(list)}")
print(f"Sum of elements = {sum(list)}")
print(f"Avg of all elements = {avg(list)}")