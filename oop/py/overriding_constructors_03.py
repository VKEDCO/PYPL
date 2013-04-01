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
        super(ThreeDPoint, this).__init__(x, y)
        this.z = z


class A:
    def __init__(this, x=0):
        this.x = x
class B:
    def __init__(this, y=0):
        this.y = y

## This does not work
class C(A, B):
    def __init__(this, x=0, y=0, z=0):
        super(C, this).__init__(x)
        super(C, this).__init__(y)
        this.z = z

