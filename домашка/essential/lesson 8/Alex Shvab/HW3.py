import random
import string
import shelve

FILENAME = "link_shorter"

while True:
    print("Select operation:")
    print("1. Take short link")
    print("2. Take original link")
    print("3. Exit")
    choose = int(input("> "))
    if choose == 1:
        with shelve.open(FILENAME) as links:
            enter_full_url = input("Enter your url: ")
            short = (random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in
                     range(random.randrange(5, 8)))
            short_link = "http://" + "".join(short)

            links[short_link] = enter_full_url
            print("Short link: ", short_link)
    elif choose == 2:
        with shelve.open(FILENAME) as links:
            short_link = input("Enter your short link: ")
            print("Full link: ", links.get(short_link, "Incorrect link"))
    else:
        print("Exit")
        break
