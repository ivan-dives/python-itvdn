def hello(name='Alex'):
    print("Hi", name, "!", sep=" ")

yourname = input("Enter your name: ")
if yourname == "":
    hello()
else:
    hello(yourname)