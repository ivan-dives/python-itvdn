string1 = set(input("Enter some string:\n>> "))
string2 = set(input("And another string:\n>> "))
eq_str = set(string1 & string2)
print(*eq_str)