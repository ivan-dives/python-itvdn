str1 = input("Enter text: ")
str2 = input("Enter other text: ")

char_set = {x for x in str1}
char_set2 = {x for x in str2}

print(char_set & char_set2)