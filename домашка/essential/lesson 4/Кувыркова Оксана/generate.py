
def reverce_list(iterable):
    i = len(iterable)
    while i:
        i -= 1
        yield iterable[i]


list = [5, 12, 'june']
new_list = reverce_list(list)
print(*new_list)