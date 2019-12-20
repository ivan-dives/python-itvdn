def prime_generator(num):
    for prime in range(1, num):
        prime += 1
        if prime == 2:
            pass
            #print(2, end=' ')
        for i in range(2, prime):
            print(f'{prime=}', f'{i=}')
            if prime % i == 0:
                print('break')
                break
        else:
            yield prime

my_set2 = set()

for f in prime_generator(20):
    #print(f'{f=}', type(f))
    #my_set2 = set()
    #my_set2 |= {f}
    print(f'{f=}', type(f))
    my_set2.add(f)
    # print(my_set, sep=' ', end=' ')
    print(my_set2, sep=' ', end='\n')

print(sorted(my_set2))
