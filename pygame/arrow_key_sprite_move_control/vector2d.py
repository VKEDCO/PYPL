import math

class Vector2D(object):
    
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    @classmethod
    def vector_from_points(cls, p1, p2):
        return cls(p2[0] - p1[0], p2[1] - p1[1])

    @classmethod
    def vector_from_vectors(cls, v1, v2):
        return cls(v2.x - v1.x, v2.y - v2.y)

    def to_point(self):
        return self.x, self.y

    def to_int_point(self):
        return int(self.x), int(self.y)
    
    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_distance_to(self, point):
        if type(point) == tuple:
            px, py = point
        elif type(point) == Vector2D:
            px, py = point.x, point.y
        else:
            raise Exception('unknown type of point')
        return math.sqrt((self.y - py)**2 + (self.x - px)**2)

    def normalize(self):
        magn = self.get_magnitude()
        if magn > 0:
            self.x /= magn
            self.y /= magn

    def get_normalized(self):
        self.normalize()
        return self

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


def test_01():
    A = (10.0, 20.0)
    B = (30.0, 35.0)
    C = (15.0, 45.0)
    AB = Vector2D.vector_from_points(A, B)
    print 'AB=', AB
    BC = Vector2D.vector_from_points(B, C)
    print 'BC=', BC
    AC = Vector2D.vector_from_points(A, C)
    print 'AC=', AC
    AB_PLUS_BC = AB + BC
    print 'AB+BC =', AB_PLUS_BC
    AB_MIN_BC = AB - BC
    print 'AB-BC =', AB_MIN_BC
    AB_TIMES_2 = AB.scale(2)
    print '2*AB =', AB_TIMES_2
    NEG_AB = -AB
    print '-AB=', NEG_AB
    print AB * 2

    
## test_01()
