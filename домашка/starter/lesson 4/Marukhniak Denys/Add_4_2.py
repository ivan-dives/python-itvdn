print('Enter your code using PEP8. If you want to finish coding enter "end":')
name = ''
value = None
while True:
    cloud = ''
    a = ''
    b = ''
    string = input()
    for i in range(len(string)):
        cloud += string[i]
        # print(cloud)
        # print('') >>>
        if cloud == "print('":
            for v1 in range(i, len(string)):
                # print('a=', a)
                a += string[v1]
                if "')" in a:
                    print(a[1:-2])
                    break
                elif "', '" in a:
                    a = a[:-4] + " "
        # print("") >>>
        elif cloud == 'print("':
            for v2 in range(i, len(string)):
                b += string[v2]
                if '")' in b:
                    print(b[1:-2])
                    break
                elif '", "' in b:
                    b = b[:-4] + " "
        # print >>>
        elif cloud == 'print(' and string[len(cloud)] != '"' and string[len(cloud)] != "'":
            if value:
                if string[len(cloud):-1] == name:
                    print(value)
                else:
                    print(f"NameError: name '{string[len(cloud):-1]}' is not defined")
        # = input >>>
        elif cloud[len(cloud)-10:] == " = input('" or cloud[len(cloud)-10:] == ' = input("':
            name = cloud[:-10]
            value = input()
        # variable num >>>
        elif cloud[len(cloud)-3:] == " = " and not string[len(cloud)] in ['"', "'", 'i']:
            name = cloud[:-3]
            value = int(string[len(cloud):])
        # variable '' >>>
        elif cloud[len(cloud)-4:] == " = '":
            name = cloud[:-4]
            value = string[len(cloud):-1]
        # variable "" >>>
        elif cloud[len(cloud)-4:] == ' = "':
            name = cloud[:-4]
            value = string[len(cloud):-1]
        # commentary >>>
        elif cloud == "#":
            pass
    # end >>>
    if string.lower() == "end":
        break
