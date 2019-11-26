def stairs(n = 0):
    if n > 0:
        def stairs_in(n):
            if n == 0 or n == 1:
                return 1
            else:
                return stairs_in(n-1) + stairs_in(n-2)
        return stairs_in(n)
x = int(input('Number of stairs: '))
print(f'Ways to climb the stairs: {stairs(x)}')
