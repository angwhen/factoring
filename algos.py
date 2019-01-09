import math
"""all methods return factors, num_steps, num_unfactored
num_unfactored of the last factors are not prime"""

def get_primes():
    p_list = []
    with open("P-10000.txt", "r") as f:
        for line in f:
            p_list.append(int(line.split(",")[1]))
    return p_list
    
#TODO: steps approp for is_square?
def is_square(x):
    return x >= 0 and int(math.sqrt(x)) == math.sqrt(x)

def gcd(A,B):
    A, B = int(A), int(B)
    steps = 0
    while B != A and  B != 0:
        steps +=1
        temp = B
        B = A % B
        A = temp
    return A, steps

def trial_division(N,when_to_stop=None):
    primes_list = get_primes()
    m, pi, p, steps = N, 0, 2, 0
    factors = []
    if when_to_stop == None:
        when_to_stop = math.sqrt(N)
    while (p <= when_to_stop):
        steps += 1
        if m % p == 0:
            m = m/p
            factors.append(p)
        else:
            pi += 1
            p = primes_list[pi]
    num_unfactored = 0
    if m != 1:
        factors.append(m)
        if m not in primes_list:
            num_unfactored = 1
    return factors,steps,num_unfactored

def fermats_diff_of_squares(N):
    return [],0,0

def harts_one_line_helper(N,L=-1):
    if L == -1:
        L = N
    steps = 0
    for i in xrange(1,L):
        steps += 1
        s = int(math.ceil(math.sqrt(N*i)))
        m = (s*s) % N
        if (is_square(m)):
            break
    t = math.sqrt(m)
    f1, gcd_steps = gcd(s-t,N) 
    f2 = N/f1
    steps += gcd_steps
    return f1, f2, steps

def harts_one_line(N):
    # check if N sqare
    primes_list = get_primes()
    factors = []
    steps = 0
    if not is_square(N):
        when_to_stop = math.pow(N,1.0/3.0)
        factors,steps,num_unfactored = trial_division(N, when_to_stop)
        
    if num_unfactored == 1: #not possible in trial division to have more unfactored
        N = factors[-1]
        #do harts one_line
        to_check = [N]
        leftover_factors = []
        while(len(to_check)>0):
            f = to_check.pop(0)
            if f == 1 or f in primes_list:
                leftover_factors.append(f)
            else:
                hf1,hf2, hart_steps = harts_one_line_helper(f)
                to_check.append(hf1)
                to_check.append(hf2)
                steps += hart_steps
        factors.extend(leftover_factors)
    return factors, steps, 0

def lehmans_var_of_fermat(N):
    return [],0,0

def lehmers_factoring_method(N):
    return [],0,0

def pollards_rho_method(N):
    return [],0,0

def pollards_pminus1_method(N):
    return [],0,0

