a = float(input("a = "))
b = float(input("b = "))


while True:
   print("1. Add")
   print("2. Minus")
   print("3. Multiply")
   print("4. Divide")
   print("5. Exit")
   response = input("Choose a nesessary option: ")
   print()
   if response == "1":
    def add_numbers(a, b):
       return a + b
    result = add_numbers(a, b)
    print(result)
    print()
    add_numbers(a, b)
   elif response == "2":
    def minus_numbers(a, b):
        return a - b
    result1 = minus_numbers(a, b)
    print(result1)
    print()
    minus_numbers(a, b)
   elif response == "3":
    def multiple(a, b):
        return a * b
    result2 = multiple(a, b)
    print(result2)
    print()
    multiple(a, b)
   elif response == "4":
    def divide(a, b):
        while b != 0:
            return a / b
        if b == 0:
            print("it's not possible to divide by 0")
    result3 = divide(a, b)
    print(result3)
    print()
    divide(a, b)
   elif response == "5":
       break
