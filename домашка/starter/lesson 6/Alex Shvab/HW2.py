str = input("Enter word: ")

def revers(word):
    revstr = word[::-1]
    return revstr

def polindrom(str1, str2):
    if str1 == str2:
        print(f"{str1}\n {str2}\n Wow it's polindrom")
    else:
        print(f"{str1}\n {str2}\n Sorry it's not polindrom")

polindrom(str, revers(str))

