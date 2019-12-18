def base(k):
    k = container.get(k)
    return k


def add_to_base(x, y):
    container[x] = y
    return container


container = {
    "https://docs.python.org/3/library/index.html": "https://goo-gl.su/python"
}

print("""\nWhich operation do you choose?:

        1) To get link enter 'get'
        2) To add link enter 'add'
        3) To find link enter 'find'
        
""")


def main():
    while True:
        ch = input()
        if ch == "find":
            find_key = input("What link are we looking for?\n ")
            new_key = find_key
            base(find_key)
            if find_key is None:
                print("no similar links found...")
                yes = input("Do you want to add? ('y' or press 'Enter'):\n ")
                if yes == "y":
                    new_var = input("Set a new link\n ")
                    add_to_base(new_key, new_var)
            else:
                print(container.get(new_key))
        elif ch == "add":
            new_key = input("Enter a new link to add\n ")
            new_var = input("and now enter a result link to set\n ")
            add_to_base(new_key, new_var)
        elif ch == "get":
            new_key = input("Enter a word to get link\n ")
            container.setdefault(new_key, "https://www.google.com/search?q=" + new_key)
            print(container.get(new_key))
        elif ch == "exit":
            exit()
        else:
            print("wrong option...")


if __name__ == '__main__':
    main()
