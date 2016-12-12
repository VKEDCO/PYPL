import math

#######################################################
## Godel numbers, compilation and reverse compilation
## author: vladimir kulyukin
#######################################################

def pair_of(x, y):
    return 2**x*(2*y + 1) - 1

def left_of(z):
    d = 0
    for i in xrange(z+1):
        if (z+1) % (2**i) == 0:
            d = i
    return d

def right_of(z):
    x = left_of(z)
    return ((z + 1)/(2**x) - 1)/2

def compile_instruction_numbers(a, b, c):
    return pair_of(a, pair_of(b, c))

def compile_instruction_pair(a_bc):
    a, bc = a_bc
    b, c = bc
    return compile_instruction_numbers(a, b, c)

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    for d in xrange(2, n/2 + 1):
        if n % d == 0:
            return False
    return True

def ith_prime(i):
    k = 1
    n = 2
    while True:
        if is_prime(n):
            if k == i:
                return n
            else:
                k += 1
        n += 1

def factors_aux(n, i, list_of_factors):
    if n == 0 or n == 1: return list_of_factors + [n]
    if is_prime(n): return list_of_factors + [n]
    pi = ith_prime(i)
    if n % pi == 0:
        return factors_aux(n/pi, i, list_of_factors + [pi])
    else:
        return factors_aux(n, i+1, list_of_factors)

def prime_factors_of(n):
    return factors_aux(n, 1, [])

def godel_number_to_natural_number(g_number):
    product = 1
    i = 1
    for power in g_number:
        product *= ith_prime(i)**power
        i += 1
    return product

def natural_number_to_godel_number(n):
    powers = {}
    if n == 0 or n == 1: return powers
    #if is_prime(n): return list_of_powers + [1]
    i = 1   
    while n > 1:
         pi = ith_prime(i)
         if n % pi == 0:
             if powers.has_key(pi):
                 powers[pi] += 1
             else:
                 powers[pi] = 1
             n = n/pi
         else:
             if not powers.has_key(pi):
                powers[pi] = 0
             i += 1
    primes = powers.keys()
    primes.sort()
    return [powers[p] for p in primes]


##Y, X1, Z1, X2, Z2, X3, Z3, X4, Z4, X5, Z5
def var_to_pos(var_name, var_subscript=1):
    if var_name == '':
        return 0
    elif var_name == 'Y':
        return 1
    elif var_name == 'X':
        return 2*var_subscript
    elif var_name == 'Z':
        return 2*var_subscript + 1
    else:
        raise Exception('Uknown variable name ' + var_name)

##Y, X1, Z1, X2, Z2, X3, Z3, X4, Z4, X5, Z5
def pos_to_var(pos):
    if pos < 1:
        raise Exception('pos must be >= 1')
    if pos == 1:
        return 'Y'
    else:
        if pos % 2 == 0:
            return 'X' + str(pos/2)
        else:
            return 'Z' + str((pos-1)/2)
    

## A1, B1, C1, D1, E1, A2, B2, C2, D2, E2
def lbl_to_pos(lbl_name, lbl_subscript=1):
    if lbl_name == '':
        return 0
    elif lbl_name == 'A':
        return 5*(lbl_subscript-1)+1
    elif lbl_name == 'B':
        return 5*(lbl_subscript-1)+2
    elif lbl_name == 'C':
        return 5*(lbl_subscript-1)+3
    elif lbl_name == 'D':
        return 5*(lbl_subscript-1)+4
    elif lbl_name == 'E':
        return 5*(lbl_subscript-1)+5
    else:
        raise Exception('Unknown label name ' + lbl_name)

## A1, B1, C1, D1, E1, A2, B2, C2, D2, E2
## A's pos = 5(sub - 1) + 1 => 5sub - 4 = pos =>
## 5sub = pos+4 => sub = (pos+4)/5 => this is A
## --------------------
## B's pos = 5(sub-1) + 2 => 5sub - 3 =>
## 5sub = pos+3 => sub = (pos+3)/5 => this is B
## --------------------
## C's pos = 5*(sub-1)+3 => 5sub - 2 =>
## 5sub = pos+2 => sub = (pos+2)/5 => this is B
## --------------------
## D's pos = 5*(sub-1)+4 = > 5sub - 1 =>
## 5sub = pos+1 => sub = (pos+1)/5 => this is D
## ---------------------
## E's pos = 5*(sub-1)+5 => 5sub - 0 =>
## 5sub = pos => sub = pos/5
def pos_to_lbl(pos):
    if pos < 1:
        raise Exception('Position cannot be less than 1')
    if (pos+4) % 5 == 0:
        return 'A' + str((pos+4)/5)
    elif (pos+3) % 5 == 0:
        return 'B' + str((pos+3)/5)
    elif (pos+2) % 5 == 0:
        return 'C' + str((pos+2)/5)
    elif (pos+1) % 5 == 0:
        return 'D' + str((pos+1)/5)
    elif pos % 5 == 0:
        return 'E' + str(pos/5)

def code_arrow_instruction(lbl, lbl_sub, var, var_sub, oper):
    a, b, c = 0, 0, 0
    a = lbl_to_pos(lbl, lbl_sub)
    c = var_to_pos(var, var_sub) - 1
    if oper == '<-':
        b = 0
    elif oper == '+':
        b = 1
    elif oper == '-':
        b = 2
    else:
        raise Exception('Unknown instruction name ' + oper)
    return (a, (b, c))
    
def code_cond_dispatch(lbl, lbl_sub, var, var_sub, goto_lbl, goto_lbl_sub):
    a, b, c = 0, 0, 0
    a = lbl_to_pos(lbl, lbl_sub)
    c = var_to_pos(var, var_sub) - 1
    b = lbl_to_pos(goto_lbl, goto_lbl_sub) + 2
    return (a, (b, c))

def problem_01():
    pairs = [
        code_arrow_instruction('B', 2, 'X', 2, '+'),
        code_arrow_instruction('', 0, 'Z', 1, '-'),
        code_cond_dispatch('', 0, 'Z', 1, 'B', 2)
        ]
    return map(lambda x: (x, compile_instruction_pair(x)), pairs)

def problem_02():
    return reverse_compile_program(20588574)

def reverse_compile_program(pn):
    g_number = natural_number_to_godel_number(pn+1)
    return map(reverse_compile_instruction, g_number)

def reverse_compile_instruction(n):
    return generate_instruction_code(reverse_compile_instruction_to_4toop(n))
    
def reverse_compile_instruction_to_4toop(n):
    a = left_of(n)
    rn = right_of(n)
    b = left_of(rn)
    c = right_of(rn)
    LBL = ''
    if a > 0:
        LBL = pos_to_lbl(a)
    INS_TYPE = ''
    if b == 0:
        INS_TYPE = '<-'
    elif b == 1:
        INS_TYPE = '+'
    elif b == 2:
        INS_TYPE = '-'
    elif b > 2:
        INS_TYPE = 'IF'
    VAR = pos_to_var(c+1)
    GOTO_LBL = ''
    if b > 2:
        GOTO_LBL = pos_to_lbl(b-2)
    return (LBL, INS_TYPE, VAR, GOTO_LBL)

def generate_instruction_code(four_toop):
    lbl, ins_type, var, goto_lbl = four_toop
    if lbl != '':
        lbl = '[' + lbl + '] '
    if ins_type == '<-':
        return lbl + var + ' ' + ins_type + ' ' + var
    if ins_type == '+':
        return lbl + var + ' <- ' + var + ' + 1'
    if ins_type == '-':
        return lbl + var + ' <- ' + var + ' - 1'
    if ins_type == 'IF':
        return lbl + ' IF ' + var + ' != 0 GOTO ' + goto_lbl
    
