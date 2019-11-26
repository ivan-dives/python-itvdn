def towers_sort(fig=1, tower1=1, tower2=2):
    if fig == 1:
        print(f"Перекладываем фигуру {fig} с башни {tower1} на башню {tower2}")
    else:
        tower3 = 6 - tower1 - tower2
        towers_sort(fig - 1, tower1, tower3)
        print(f"Перекладываем фигуру {fig} с башни {tower1} на башню {tower2}")
        towers_sort(fig -1, tower3, tower2)


towers_sort(fig=(int(input("Введите число равное высоте башни:  "))))