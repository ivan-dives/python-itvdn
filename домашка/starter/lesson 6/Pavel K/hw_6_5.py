n = 0
def move(height,A, B, C):
    if height >= 1:
        move(height-1,A,C,B)
        print(f' move {A} -> {B}')
        move(height-1,C,B,A)
        global n
        n += 1

z = int(input('How tall is your tower?'))
move(z, "1","2","3")

print(f' all you need to do {n} movements')