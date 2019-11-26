#это еще один способ кроме [::-1}, но правда сложнее, но еще один вариант)))

def palindrome(word="mom"):
    if len(word) == 3:
        if word[0] == word[2]:
            print(f"Слово '{word}' полиндром")
        else:
            print(f"Слово '{word}' не полиндром")
    elif word[0] == word[-1] and palindrome(word[1:-1]):
        print(f"Слово '{word}' это полиндром =)")
    else:
        print(f"Слово '{word}' не полиндром")

word = input("Введи сло и я попробую угадать полиндром это или неи: ")
palindrome(word)