import func_mod


def user_input():
    print("""\nWhich operation do you choose?:
    
                1) To get link enter 'get'
                2) To add link enter 'add'
                3) To find link enter 'find'
    
        """)
    while True:
        ch = input()
        if ch == "find":
            find_key = input("What link are we looking for?\n ")
            new_key = find_key
            sw = func_mod.get_data(find_key)
            if sw is None:
                print("no similar links found...")
                yes = input("Do you want to add? ('y' or press 'Enter'):\n ")
                if yes == "y":
                    new_var = input("Set a new link\n ")
                    container = {new_key: new_var}
                    func_mod.put_data(container)
                else:
                    pass
            else:
                print(func_mod.get_data(find_key))
        elif ch == "add":
            new_key = input("Enter a new link to add\n ")
            new_var = input("and now enter a result link to set\n ")
            container = {new_key: new_var}
            func_mod.put_data(container)
            print("add complete..")
        elif ch == "get":
            new_key = input("Enter a word to get link\n ")
            temp = (new_key, f"{func_mod.URL_SHORT_LINK}/{new_key}")
            print(temp)
            func_mod.put_default_data(temp)
        elif ch == "exit":
            exit()
        else:
            print("wrong option...")
