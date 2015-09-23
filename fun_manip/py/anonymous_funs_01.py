import sys

#################################################
#
# anonymous_funs_01.py
# Examples of generating functions dynamically
# author: Vladimir Kulyukin
#
#################################################

def make_adder(n):
    return lambda x: x + n

def make_another_adder(n):
    def add(x): return x + n
    return add

def make_multiplier(k):
    return lambda x: k*x

def make_another_multiplier(k):
    def mult(x): return k*x
    return mult

def test_adders():
    add3 = make_adder(3)
    add4 = make_adder(4)
    print 'Testing adders...'
    for x in xrange(1, 6):
        sys.stdout.write('add3(' + str(x) + ')=' + str(add3(x))+"\n")
        sys.stdout.write('add4(' + str(x) + ')=' + str(add4(x))+"\n")

def test_multipliers():
    mult3 = make_multiplier(3)
    mult4 = make_multiplier(4)
    print 'Testing multipliers...'
    for x in xrange(1, 6):
        sys.stdout.write('mult3(' + str(x) + ')=' + str(mult3(x))+"\n")
        sys.stdout.write('mult4(' + str(x) + ')=' + str(mult4(x))+"\n")
        
test_adders()
test_multipliers()
