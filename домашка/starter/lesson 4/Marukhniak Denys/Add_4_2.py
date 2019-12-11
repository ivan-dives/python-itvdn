print('Enter your code using PEP8. If you want to finish coding enter "end":')
name = ''
value = ''
while True:
    cloud = ''
    cloud_s = ''
    a = ''
    b = ''
    string = input()
    for i in range(len(string)):
        cloud += string[i]
        # print(cloud)
        # print('') >>>
        if "#" in cloud:
            pass
        elif cloud == "print('":
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
                if string[len(cloud):len(cloud)+len(name)] == name and string[len(cloud)+len(name)] == ')':
                    print(value)
                else:
                    print(f"NameError: name '{string[len(cloud):len(cloud)+len(name)]}' is not defined")
        # = input >>>
        elif cloud[len(cloud)-10:] == " = input('" or cloud[len(cloud)-10:] == ' = input("':
            name = cloud[:-10]
            value = input()
        # variable num >>>
        elif cloud[len(cloud)-3:] == " = " and not string[len(cloud)] in ['"', "'", 'i']:
            name = cloud[:-3]
            for num in range(len(cloud), len(string)):
                if string[num] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    value += string[num]
                else:
                    break
            value = int(value)
        # variable '' >>>
        elif cloud[len(cloud)-4:] == " = '":
            name = cloud[:-4]
            value = ''
            for num in range(len(cloud), len(string)):
                if string[num] != "'":
                    value += string[num]
                else:
                    break
            print(value, '11')
            print(name, '22')
        # variable "" >>>
        elif cloud[len(cloud)-4:] == ' = "':
            name = cloud[:-4]
            value = ''
            for num in range(len(cloud), len(string)):
                if string[num] != '"':
                    value += string[num]
                else:
                    break
    # end >>>
    if string.lower() == "end":
        break
