

def name_hi(my_name="Dima"):
    print(f"My name is {my_name}!")

name = input("Hello! What is your name?:  ")
if name == "":
    name_hi()
else:
    name_hi(name)





