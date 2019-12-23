
try:
    amount = int(input("How many links will you have?\n"))
    link_dict = {}
    for i in range(amount):
        long = input("full link:").lower()
        short = input("Short link:").lower()
        link_dict[short] = long
    print(link_dict.get(str(input("Enter short name of the link you would like to get"))))
except ValueError:
    print("You entered invalid value\n")


