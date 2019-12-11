slovo = str(input("Введите слово: "))
a = slovo[::-1]

if slovo == a:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")