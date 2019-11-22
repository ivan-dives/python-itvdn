def hello(name='Alex'):
    if name == "":
        print("Hi Alex!")
    else:
        print(f"Hi {name} !")

yourname = input("Enter your name: ")

hello(yourname)