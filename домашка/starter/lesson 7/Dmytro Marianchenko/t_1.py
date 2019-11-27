
conteiner=[]


while True:
    a = input("Input any number i any range (to exit input 'done'):  ")
    if a.isdigit():
        a = int(a)
        conteiner.append(a)
    elif a == "done":
        break
    else:
        pass

print(f"Your list is '{conteiner}'")

while True:
    sort = input("Do you want to sort your list? y/n:  ")
    if sort == "y":
        conteiner.sort()
        print()
        print(f"Your list is sorted, now it looks like this: {conteiner}")
        print()
        print(f"Max value of your list is '{conteiner[-1]}' and min value is '{conteiner[0]}")
        break
    elif sort == "n":
        conteiner_sorted = conteiner.copy()
        conteiner_sorted.sort()
        print()
        print(f"Ok you list not sorted and looks like this: {conteiner}")
        print()
        print(f"Max value of your list is '{conteiner_sorted[-1]}' and min value is '{conteiner_sorted[0]}")
        break
    else:
        print(f"{sort} wrong answer...")
        pass




print(f"Sum of your list is '{int(sum(conteiner))}'")
print(f"Arithmetic mean of yor list is '{int(sum(conteiner)/len(conteiner))}' =)")