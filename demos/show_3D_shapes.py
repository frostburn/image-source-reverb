from pylab import *
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from image_source_reverb.shapes import *


points = randn(10000, 3)
for d in exp(linspace(1, 0, 100)):
    for point in points:
        if regular_tetrahedron.contains(point):
            point *= d
        else:
            point /= d

x, y, z = points.T

fig = figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z, ".")
show()


points = randn(10000, 3)
for d in exp(linspace(1, 0, 100)):
    for point in points:
        if regular_dodecahedron.contains(point):
            point *= d
        else:
            point /= d

x, y, z = points.T

fig = figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z, ".")
show()
