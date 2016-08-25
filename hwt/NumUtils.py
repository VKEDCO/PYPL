import math
import random

### Module: NumUtils.py
### Author: Vladimir Kulyukin

class NumUtils:

    @staticmethod
    def isPowOf2(n):
        if n < 1:
            return False
        else:
            pOf2 = (math.log(n)/math.log(2))
            return math.fabs(pOf2 - int(pOf2)) == 0

    @staticmethod
    def intLog2(n):
        return int(math.log(n)/math.log(2))

    @staticmethod
    def genListOfRandomInts(a, b, num_elems):
        return [random.randint(a, b) for i in xrange(num_elems)]

    @staticmethod
    def areEqualLists(lst1, lst2):
        if len(lst1) != len(lst2):
            return False
        for x, y in zip(lst1, lst2):
            if x - y != 0:
                return False
        return True

    
        


