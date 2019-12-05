class Foot:
    def qw(self):
        print('меня едят')

class Cherry(Foot):
    def ty(self):
        print('я красное')

class Apple(Foot):
    def po(self):
        print('я зеленое')

class Fruits(Cherry, Apple):
    def ui(self):
        print('я росту на дереве')

def ch():
    fr = Fruits()
    fr.qw()
    fr.ty()
    fr.ui()
def ap():
    fr = Fruits()
    fr.qw()
    fr.po()
    fr.ui()

if __name__ == '__main__':
    ch()
    print()
    ap()

print()
for cls in [Foot, Cherry, Fruits]:
    print(cls. __name__+ '-',cls.mro())
print()
for cls in [Foot, Apple, Fruits]:
    print(cls. __name__+ '-',cls.mro())