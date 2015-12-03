#!/usr/bin/python

import math

class Vector2D(object):

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    ## equivalent of static methods
    @classmethod
    def vector_from_points(vcls, p1, p2):
        return vcls(p2[0] - p1[0], p2[1] - p1[1])

    @classmethod
    def vector_from_vectors(vcls, v1, v2):
        return vcls(v2.x - v1.x, v2.y - v2.y)

    ## convert this vector to a 2-tuple of numbers
    def to_point(self):
        return self.x, self.y

    ## convert this vector to 2-tuple of ints
    def to_int_point(self):
        return int(self.x), int(self.y)

    ## compute the vec's magnitude
    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    ## compute the distance to a point
    def get_distance_to(self, point):
        if type(point) == tuple:
            px, py = point
        elif type(point) == Vector2D:
            px, py = point.x, point.y
        else:
            raise Exception('unknown type of point')
        return math.sqrt((self.y - py)**2 + (self.x - px)**2)

    ## get the unit vector
    def normalize(self):
        magn = self.get_magnitude()
        if magn > 0:
            self.x /= magn
            self.y /= magn

    def get_normalized(self):
        self.normalize()
        return self

    ## Py does not operator overloading but does have magic methods
    def __add__(self, rhs):
        return Vector2D(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Vector2D(self.x - rhs.x, self.y - rhs.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def scale(self, scalar):
        return Vector2D(self.x*scalar, self.y*scalar)

    def __mul__(self, scalar):
        return Vector2D(self.x*scalar, self.y*scalar)

