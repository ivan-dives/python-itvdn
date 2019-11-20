height = int(input('Height: '))
step = int(input('Step: '))
sp = (height - 1)*step
sp_x = sp
ch = 1
ch_x = ch
while True:
    char = input('Character: ')
    if len(char) == 1:
        while height > 0:
            while ch > 0:
                while sp > 0:
                    print(' ', end='')
                    sp -= 1
                print(char, end='')
                ch -= 1
            print()
            sp = sp_x - step
            sp_x = sp
            ch = ch_x + 2*step
            ch_x = ch
            height -= 1
        break
    else:
        print('Only one character allowed!')
input("Press 'Enter' to exit")