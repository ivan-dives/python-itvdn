
def prime_generator(num):
    for prime in range(1, num):
        prime += 1

        for i in range(2, prime):
            if prime % i == 0:
                break
        else:
            yield prime

my_set2 = set()
for f in prime_generator(20):
    my_set2.add(f)
print(my_set2, sep=' ', end='\n')