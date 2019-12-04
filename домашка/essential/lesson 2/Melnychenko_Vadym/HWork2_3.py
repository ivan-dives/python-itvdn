class Editor(): pass

class ProEditor(Editor): pass

class Viewing(ProEditor): pass

class ProViewing(Viewing): pass

print(Editor.__mro__)
print(ProEditor.__mro__)
print(Viewing.__mro__)
print(ProViewing.__mro__)
