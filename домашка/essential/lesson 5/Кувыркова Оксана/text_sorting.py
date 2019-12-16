
words = input("Please enter any words using space\n")
new_str = words.split()
new_str.sort()

print(', '.join(map(str, new_str)))