# OrderedDict

# The list of samples
measure = [("ft", "foot"), ("in", "inch"), ("mm", "millimeter"), ("cm", "centimeter"), ("yd", "yard"), ("mi", "mile")]
# The dictionary sample
lim_dict = {}
for name, mesuring in measure:
    lim_dict[name] = mesuring
print(lim_dict.keys())
print(lim_dict.values())

from collections import OrderedDict
# New ordered dictionary - order the same as in first list
o_lim = OrderedDict(measure)

print(o_lim.keys())
print(o_lim.values())


# Defaultdict
name = "In this text will be checked all letters quantity of includings"
new_name = name.replace(" ", "")
d = {}
for i in new_name:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1
from collections import defaultdict

d = defaultdict(int)
for i in new_name:
    # and here we are increasing numbers from "0' every time once it will be founded in "new_name"
    d[i] += 1
# each elemet int dictionary "d" receiving default value equal"0" automaticly:


# ChainMap
from collections import ChainMap

lim2_dict = {'lb': 'pound', 'oz': 'ounce', 'kg': 'kilogram', 'pt': 'pint'}
list3 = list(ChainMap(lim_dict, lim2_dict))
print(list3)

print(ChainMap(lim_dict, lim2_dict))