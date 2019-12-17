# Напишите программу, которая вводит с клавиатуры последовательность чисел и выводит её
# отсортированной в порядке возрастания.


def is_numb_val(val):
    try:
        x = float(val)
    except ValueError:
        return False
    else:
        return True

def main():
    num_seq = input("Введите последовательность чисел через пробел: ").split()
    num_lst = [float(s) for s in num_seq if is_numb_val(s)]
    print(sorted(num_lst))


if __name__ == '__main__':
    main()
