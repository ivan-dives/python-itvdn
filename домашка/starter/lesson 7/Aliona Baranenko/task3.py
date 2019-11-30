
my_list = [1, 4, 8, 25, 6, 14]


while True:
    print("options")
    print("1. sum ")
    print("2.multiply ")
    print("3.exit ")
    response = input("choose your option - ")
    print()
    if response == "1":
        print(sum(my_list))
    elif response == "2":
        def multiply(my_list):
            answer = 1
            for i in my_list:
                answer *= i
            return answer
        print(multiply(my_list))
    elif response == "3":
        break
    else:
        print("incorrect choice")
        break


def primenumbers(my_list):
    if n == 1:
        return False
    for x in range(2, my_list):
        if n % x == 0:
            return False
        else:
            return True

print(primenumbers(my_list))