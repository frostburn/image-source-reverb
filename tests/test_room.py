import numpy as np
from image_source_reverb.room import Plane, Room

def test_mirrors_origin():
    p = Plane([1, 0], distance=1.1)
    x = p.mirror_point([0, 0])
    assert np.allclose(x, [-2.2, 0])


def test_ignores_backside():
    p = Plane([2, 1])
    assert p.mirror_point([-2, -2]) is None


def test_triangle_reflections():
    r = Room([[0, 1], [1, -1], [-1, -1]])
    reflections = r.reflect_points([[0, 0]])
    assert np.allclose(reflections, [
        [0, -2],
        [-np.sqrt(2), np.sqrt(2)],
        [np.sqrt(2), np.sqrt(2)]
    ])
