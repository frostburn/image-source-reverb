from pylab import *
from image_source_reverb.shapes import *


def inside_triangle(x, y):
    return equilateral_triangle.contains([x, y])


def inside_pentagon(x, y):
    return equilateral_pentagon.contains([x, y])

inside_triangle = frompyfunc(inside_triangle, 2, 1)
inside_pentagon = frompyfunc(inside_pentagon, 2, 1)


x = linspace(-2.5, 2.5, 256)
x, y = meshgrid(x, x)

data = inside_triangle(x, y).astype(float)
imshow(data)
show()

data = inside_pentagon(x, y).astype(float)
imshow(data)
show()
