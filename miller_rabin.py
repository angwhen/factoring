import math
import random

# write n-1 as 2^r*d, d is odd
# return r, d
def write_as_power_of_two_times_odd_helper(n):
    d = n-1
    r = 0
    while d % 2 == 0:
        d = d/2
        r += 1
    return r, d

# returns True if probably prime, false else
def miller_rabin(n, k=5):
    steps = 0
    if n == 1:
        return False, steps
    if n == 2 or n ==3:
        return True,steps
    steps += 1 
    if n % 2 == 0:
        return False,steps

    steps += 1
    r,d = write_as_power_of_two_times_odd_helper(n)
    #print r,d
    for i in xrange(0,k):
        can_continue = False
        a = random.randint(2,n-2)
        x = (a**d)% n 
        steps +=1
        if x == 1 or x == n-1:
            continue
        for j in xrange(0,r-1):
            x = x**2 % n 
            steps += 1
            if x == n-1:
                can_continue = True
                break
        if can_continue:
            continue 
        else:
            return False, steps
    return True, steps

#TODO
def miller_rabin_deterministic(n):
    if n == 2 or n == 3:
        return True, 0
    return None, 0 

# resources:
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test


# TODO: visualizations for patterns of witnesses?

