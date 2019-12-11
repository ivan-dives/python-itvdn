a = 10
b = 20
lst = [i for i in range(a, b+1)]

def for_check(a,b):
    sum = 0
    for i in range(a, b+1):
        sum += i
    return sum

def while_check(a,b, step=-1):
    sum = 0
    while a <= b:
        sum += a
        a += 1
    else:
        for i in range(a, b-1, step):
            sum += i
    return sum

# should be unit test :)
print(f"Robe summ is: {for_check(a,b)}" if for_check(a,b) == sum(lst) else f"Ne Robe your sum is {for_check(a,b)} must be {sum(lst)}")
print(f"While sum = {while_check(b, a)}")
