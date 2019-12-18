import random
import string

full_url = {}
short_url = {}

while True:
    print("""Select operation:
    1. Take short link
    2. Take original link
    3. Exit""")
    choose = int(input("> "))
    if choose == 1:
        enter_full_url = input("Enter your url: ")
        short_link = "http://" + "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in
                                         range(random.randrange(5, 8)))

        full_url[enter_full_url] = short_link
        short_url[short_link] = enter_full_url
        print("Short link: ", short_link)
    elif choose == 2:
        short_link = input("Enter your short link: ")
        print("Full link: ", short_url.get(short_link, "Incorrect link"))
    else:
        print("Exit")
        break


# print(full_url)
# print(short_url)