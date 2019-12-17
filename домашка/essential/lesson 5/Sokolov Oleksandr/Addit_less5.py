try:
    my_list = []
    while True:
        my_list.append(int(input('Enter number:')))
        my_list_sorted = sorted(my_list)
except ValueError:
    print("You entered no integer, try again")
print(my_list_sorted)


