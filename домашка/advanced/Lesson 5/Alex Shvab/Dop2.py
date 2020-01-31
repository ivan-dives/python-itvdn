import numpy


create = numpy.arange(1, 197)
mat1 = create.reshape((14, 14))
mat1 = mat1.T
mat1 = mat1 ** 2
mat1 = mat1 * 2
mat_eye = numpy.eye(14)
res = mat1 - mat_eye
print(mat1)