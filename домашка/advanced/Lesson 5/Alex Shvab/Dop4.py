import numpy


a = numpy.arange(1, 301)
a.resize((3, 100))

a2 = a.reshape((6, 50))
print(a)
print(a2)