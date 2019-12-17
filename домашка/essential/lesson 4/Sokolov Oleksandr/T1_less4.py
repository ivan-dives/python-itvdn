class Reversedword:

    def __init__(self, text):
        self.text = text
        self.index = len(text)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.text[self.index]

rever = Reversedword('timil on sah noitcefreP')
for word in rever:
    print(word, end='')

