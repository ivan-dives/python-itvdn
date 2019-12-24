
def user_dialog():
    try:
        amount = int(input("How many links will you have?\n"))
        long = input("full link:").lower()
        short = input("Short link:").lower()
        return amount, long, short
    except ValueError:
        print("You entered invalid value\n")

