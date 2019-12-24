import random

with open("some_text.txt", "w") as f:
    lst = [random.uniform(1, 10000) for x in range(10000)]
    for i in lst:
        f.write(f"{i}\n")

with open("some_text.txt", "r") as f:
    result = []
    for line in f.readlines():
        temp = [float(line) for i in line.split(",") if i.strip()]
        result += temp

print(sum(result))





