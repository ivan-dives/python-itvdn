
conteiner=[]
a = 0

while True:
    #

print(f"Your list is '{conteiner}'")

while True:
    sort = input("Do you want to sort your list? y/n:  ")
    if sort == "yes":
        conteiner.sort()
        print(f"Your list is sorted, now it looks like this: {conteiner}")
        print()
        print(f"Max value of your list is '{conteiner[-1]}' fnd min value is '{conteiner[0]}")
        break
    elif sort == "n":
        conteiner_sorted = conteiner.copy()
        print(f"Ok you list not sorted and looks like this: {conteiner}")
        print()
        print(f"Max value of your list is '{conteiner_sorted[-1]}' fnd min value is '{conteiner_sorted[0]}")
        break
    else:
        print(f"{sort} wrong answer...")
        pass

print(conteiner(type))

print()
print(f"Sum of your list is '{sum(conteiner)}'")
print()
print(f"Arithmetic mean of yor list is '{sum(conteiner)/len(conteiner)}' =)")