__metaclass__ = type

import math

class TwoDPoint:
    def __init__(this, x=0, y=0):
        this.x = x
        this.y = y
    def dist_from_origin(this):
        math.hypot(this.x, this.y)

class ThreeDPoint(TwoDPoint):
    def __init__(this, x=0, y=0, z=0):
        TwoDPoint.__init__(this, x, y)
        this.z = z


class A:
    def __init__(this, x=0):
        this.x = x

class B:
    def __init__(this, y=0):
        this.y = y

class C(A, B):
    def __init__(this, x=0, y=0, z=0):
        A.__init__(this, x)
        B.__init__(this, y)
        this.z = z


