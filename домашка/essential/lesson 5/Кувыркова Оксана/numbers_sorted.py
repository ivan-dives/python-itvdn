# using text method
numbers = input("Please enter any words numbers space\n")
new_num = numbers.split()
new_num.sort()

print(', '.join(map(str, new_num)))

# using list method
numbers = input("Please enter any words numbers space\n",)
numbers = [int(n) for n in numbers.split()]
new_num = sorted(numbers)

print(new_num)