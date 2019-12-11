class C:

    def __init__(self, str):
        self.str = str
        self.index = len(str) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            latter = self.str[self.index]
            if self.index < 0:
                raise StopIteration
            self.index -= 1
            return latter


str = input("Enter some string: ")
c = C(str)
res = ""
for x in c:
    res += x

print(res)
