"""     Top           Top2
       /   \        /    \
      /     \      /      \
Middle       Middle2       Middle3
     \          |           /
      \         |          /
       \        |         /
        \       |        /
             Bottom
"""




class Top:
    pass

class Top2:
    pass

class Middle(Top):
    pass

class Middle2(Top, Top2):
    pass

class Middle3(Top2):
    pass

class Bottom(Middle, Middle2, Middle3):
    pass


create = Bottom()
print(Bottom.__mro__)
