def hanoi(height = 1, rod1 = 1, rod3 = 3):
    if height == 1:
        print(f'Move disk from <<rod {rod1}>> to <<rod {rod3}>>')
    else:
        rod2 = 6 - rod1 - rod3
        hanoi(height - 1, rod1, rod2)
        print(f'Move disk from <<rod {rod1}>> to <<rod {rod3}>>')
        hanoi(height - 1, rod2, rod3)
h = int(input('Tower height: '))
hanoi(h)