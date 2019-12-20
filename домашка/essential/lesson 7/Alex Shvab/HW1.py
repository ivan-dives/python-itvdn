import url_work as  uw

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
        print("Short link: ", uw.cut_url(enter_full_url))
    elif choose == 2:
        short_link = input("Enter your short link: ")
        print("Full link: ", uw.full_url(short_link))
    else:
        print("Exit")
        break
