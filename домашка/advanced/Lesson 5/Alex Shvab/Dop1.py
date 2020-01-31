import numpy


create = numpy.arange(1, 626)
mat1 = create.reshape((25, 25))

mat_eye = numpy.eye(25)
res = mat1 * mat_eye
print(res)