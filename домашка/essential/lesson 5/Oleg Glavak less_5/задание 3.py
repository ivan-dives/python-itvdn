text = input("Введите текст - ")

print(sorted(text.split(), key=str.lower))