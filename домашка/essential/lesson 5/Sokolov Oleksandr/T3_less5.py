input_str = input("Enter a string: ")

words = input_str.split()

words.sort()

print("The sorted words are:")
for word in words:
    print(word, end=' ')


