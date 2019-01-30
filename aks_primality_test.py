import math

# returns true/false, steps
# returns true if m is of the form n^k for integers n>=2 and k >=2
# steps is # of power operations
def is_power_helper(m):
    steps = 0
    k = 2
    for n in xrange(n,m/2): # will break out earlier
        while True:
            steps += 1 
            p = math.pow(n,k)
            if m == p:
                return True, steps
            elif p > m:
                if k == 2:  # got too big without matching
                    return False, steps 
                else:
                    k = 2
                    break
            else:
                k += 1
    raise Exception('bug in is_power_helper, shouldn\'t reach this line...')

def largest_prime_factor_of_helper(N):
    return None, 0

def final_equality_helper(m,b,s):
    y = [0]*(s-1) # or s?
    z = [0]*(s-1)
    y[0] = 1
    z[0] = b
    z[1] = 1
    while (e > 0):


    return None,0

#TODO: CHECK steps approp for is_prime
def is_prime(x):
    if m % 2 == 0:
        return False, 0

    is_power, steps = is_power_helper(m)    
    if is_power:
        return False, steps
    
    L = math.floor(log(m)/log(2))+1
    s = 2
    while s < m:
        g, gcd_steps = gcd(m,s)
        steps += gcd_steps
        if g > 1:
            return False,steps

        isp, isp_steps = is_prime(s)
        steps += isp_steps
        if isp:
            q, q_steps = largest_prime_factor_of_helper(s-1)
            steps += q_steps
            if q>= 6 * math.sqrt(s)*L and math.pow(m,(s-1.0)/q) % s != 1:
                break
        s +=1
        
    for b in xrange(1,3*math.sqrt(s)*L):
        feh, feh_steps =  final_equality_helper(m,b,s):
        steps += feh_steps
        if feh:
            return False,steps
    return True, steps

#references: https://www.scottaaronson.com/writings/prime.pdf
