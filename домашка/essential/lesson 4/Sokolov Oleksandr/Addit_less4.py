def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True
def primes(n = 1):
    while(True):
        if isprime(n):
            yield n
        n += 1
for n in primes():
    if n > 50: break
    print(n)

# def rev_str(my_str):
#     length = len(my_str)
#     for i in range(length - 1,-1,-1):
#         yield my_str[i]
#
# for char in rev_str("hello"):
#      print(char, end='')