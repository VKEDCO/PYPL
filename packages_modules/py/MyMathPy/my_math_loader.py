import sys

## change this root dir appropriately
my_math_path = 'c:\\vladimir\\programming\\py\\MyMathPy\\'

if __name__ == '__main__':
    if not my_math_path in sys.path:
        sys.path.append(my_math_path)

## import mod_constants
## import everything from packages pack_add, pack_mult,
## and pack_subt
from pack_add  import *
from pack_mult import *
from pack_subt import *
