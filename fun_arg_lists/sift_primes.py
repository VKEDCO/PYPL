## author: Vladimir Kulyukin
import math

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    for d in xrange(2, int(math.sqrt(n))+1):
        if n % d == 0: return False
    return True

def sift_primes(prime_pred, num_list):
    lst = []
    for n in num_list:
        if prime_pred(n):
            lst.append(n)
    return lst

print sift_primes(is_prime, range(0, 31))
