def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

print ("1 Addition \n2 Subtraction \n3 Multiplication \n4 Division \n5 Quit")

while True:
    choice = input("your choise: ")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print("summ = ", add(num1, num2))
        elif choice == '2':
            print("subtraction =", subtract(num1, num2))
        elif choice == '3':
            print("multiplication =", multiply(num1, num2))
        elif choice == '4':
            print("division =", divide(num1, num2))
        else:
            break
    except ZeroDivisionError:
        print("not valid operation")
    except ValueError:
        print("not valid operation")


