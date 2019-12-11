start = int(input("enter 1st number: _"))
end = int(input("enter last number: _"))


def summ(end):

    if end < start:
        return ("Error")
    if end == start:
        return (start)
    else:
        while end > start:
            return end + summ(end - 1)

print("The sum is ", summ(end))

