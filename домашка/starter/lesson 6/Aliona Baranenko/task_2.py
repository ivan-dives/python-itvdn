def reversed(string):
    reversed_string = ''
    for i in string:
        reversed_string = i+reversed_string
    print('reversed string is: ', reversed_string)
    if string == reversed_string:
        print("it's a palindrome")
    else:
        print("it's not a palindrome")

string = input('enter a string: ')
print('entered string', string)
reversed(string)