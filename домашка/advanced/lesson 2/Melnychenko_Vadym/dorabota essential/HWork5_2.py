def average(*numbers):
    return sum(numbers) / len(numbers)


def main():

    print(average(5, 9, 25))
    print(average(*range(10)))


if __name__ == '__main__':
    main()
