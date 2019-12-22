import calendar
import heapq
import bisect
import array
import enum

a = calendar.TextCalendar(firstweekday=0)
print(a.formatyear(2019))

lst = [-3, 2, 0, 14, 5]
heapq.heapify(lst)
print(list(lst))
heapq.heappush(lst, 100)
print(list(lst))
print(heapq.heappop(lst))
print(list(lst))
print()

lst2 = [-3, 2, 0, 14, 5]
bisect.insort_right(lst2, 2)
print(lst2)
print()

a = array.array('d', [2.2, 4.1, 7.9, 0.1])
print(a)
a.append(1.8)
print(a)
print(a.buffer_info())
a.tolist()
print()

class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)
print(repr(Color.RED))
for color in Color:
    print(color)