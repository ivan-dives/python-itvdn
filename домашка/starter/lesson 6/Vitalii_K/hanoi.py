def hanoi(h = 1, r_def = 1, r_tar = 3, r_tmp = 2):
    n = 0
    def hanoi_inner(h, r_def, r_tar, r_tmp):
        nonlocal n
        if h > 0:
            hanoi_inner(h - 1, r_def, r_tmp, r_tar)
            print(f'Move disk from <<{r_def}>> \tto\t <<{r_tar}>>')
            hanoi_inner(h - 1, r_tmp, r_tar, r_def)
            n +=1
    hanoi_inner(h, r_def, r_tar, r_tmp)
    return n
height = int(input('Tower height:'))
rdef = '1st Rod'
rtar = '3rd Rod'
rtmp = '2nd Rod'
moves = hanoi(height, rdef, rtar, rtmp)
print(f'Optimal moves count is: {moves}')
