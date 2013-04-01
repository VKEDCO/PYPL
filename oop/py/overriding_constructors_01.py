__metaclass__ = type

import math

class TwoDPoint:
    def __init__(this, x=0, y=0):
        this.x = x
        this.y = y
    def dist_from_origin(this):
        math.hypot(this.x, this.y)

class ThreeDPoint(TwoDPoint):
    def __init__(this, z=0):
        this.z = z

