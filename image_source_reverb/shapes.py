import numpy as np
from numpy import sqrt
from .room import Room


def equilateral(num_sides):
    normals = [[np.cos(2*np.pi/num_sides * i), np.sin(2*np.pi/num_sides * i)] for i in range(num_sides)]
    return Room(normals)


equilateral_triangle = equilateral(3)
square = equilateral(4)
equilateral_pentagon = equilateral(5)
equilateral_hexagon = equilateral(6)
equilateral_heptagon = equilateral(7)
equilateral_octagon = equilateral(8)

regular_tetrahedron = Room([
    [1, 0, -1/sqrt(2)],
    [-1, 0, -1/sqrt(2)],
    [0, 1, 1/sqrt(2)],
    [0, -1, 1/sqrt(2)],
])

cube = Room([
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0,],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1],
])

regular_octahedron = Room([
        [1, 1, 1],
        [-1, 1, 1],
        [1, -1, 1],
        [-1, -1, 1],
        [1, 1, -1],
        [-1, 1, -1],
        [1, -1, -1],
        [-1, -1, -1],
])

def _make_dodecahedron():
    phi = 0.5 * (1+sqrt(5))
    normals = []
    for s1 in [-1, 1]:
        for s2 in [-phi, phi]:
            normal = [0, s1, s2]
            for _ in range(3):
                normals.append(normal[:])
                normal = [normal[2], normal[0], normal[1]]
    return normals

regular_dodecahedron = Room(_make_dodecahedron())

def _make_icosahedron():
    phi = 0.5 * (1+sqrt(5))
    normals = []
    for s1 in [-1, 1]:
        for s2 in [-1, 1]:
            for s3 in [-1, 1]:
                normal = [s1, s2, s3]
                normals.append(normal)
                normals.append([0, s1*phi, s2/phi])
                normals.append([s2/phi, 0, s1*phi])
                normals.append([s1*phi, s2/phi, 0])
    return normals

regular_icosahedron = Room(_make_icosahedron())
