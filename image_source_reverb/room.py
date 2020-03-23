import numpy as np


class Plane(object):
    """
    N-dimensional reflective "plane"
    """

    def __init__(self, normal, distance=1):
        normal = np.array(normal)
        norm = np.linalg.norm(normal)
        self.normal = normal / norm
        self.distance = distance

    def distance_to_point(self, x):
        return np.dot(x, self.normal) + self.distance

    def mirror_point(self, x):
        x = np.array(x)
        distance = self.distance_to_point(x)
        if distance < 0:
            return None
        return x - self.normal * (2*distance)


class Room(object):
    """
    A room with perfectly reflective flat sides for echo modeling.
    """

    def __init__(self, planes):
        planes = [plane if isinstance(plane, Plane) else Plane(plane) for plane in planes]
        self.planes = planes

    def reflect_points(self, points):
        result = []
        for plane in self.planes:
            for point in points:
                point = plane.mirror_point(point)
                if point is not None:
                    result.append(point)
        return result

    def contains(self, point):
        for plane in self.planes:
            if plane.distance_to_point(point) < 0:
                return False
        return True

    def reflections(self, point, iterations, flat=True):
        result = [[point]]
        for _ in range(iterations):
            result.append(self.reflect_points(result[-1]))
        if not flat:
            return result
        images_and_signs = []
        for i, points in enumerate(result):
            images_and_signs.extend([(point, (-1)**i) for point in points])
        return images_and_signs
