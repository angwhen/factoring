import math
import trial_division

def is_square(x):
    return x >= 0 and int(math.sqrt(x)) == math.sqrt(x)

def gcd(A,B,ret_steps = False):
    A = int(A)
    B = int(B)
    num_steps = 1
    while B != A and  B != 0:
        temp = B
        B = A % B
        A = temp
        num_steps +=1
    if ret_steps:
        return A, num_steps
    return A

def harts_one_line_algo(N,L=-1,ret_steps=False):
    if L == -1:
        L = N
    num_steps = 0
    for i in xrange(1,L):
        s = int(math.ceil(math.sqrt(N*i)))
        m = (s*s) % N
        num_steps +=1
        if (is_square(m)):
            break
    t = math.sqrt(m)
    f1,gcd_steps = gcd(s-t,N,ret_steps=True) 
    f2 = N/f1
    num_steps += gcd_steps
    if ret_steps:
        return f1,f2, num_steps
    return f1,f2

def trial_division_start(N,ret_steps=False):
    #stop when p = N^1/3
    primes_list = trial_division.get_primes()
    m = N
    pi = 0
    factors = []
    p = 2
    num_steps = 0
    while (p <= math.pow(N,1.0/3.0)):
        if m % p == 0:
            m = m/p
            factors.append(p)
        else:
            pi += 1
            p = primes_list[pi]
        num_steps +=1
    if ret_steps:
        return factors,m,num_steps
    return factors,m

def harts_wrapper(N,ret_steps=False):
    # check if N sqare
    primes_list = trial_division.get_primes()
    factors_so_far = []
    num_steps = 0
    if not is_square(N):
        factors_so_far,N,num_steps = trial_division_start(N,ret_steps=True)
    if N != 1:
        #do harts one_line
        to_check = [N]
        leftover_factors = []
        while(len(to_check)>0):
            #print to_check
            f = to_check.pop(0)
            if f == 1 or f in primes_list:
                leftover_factors.append(f)
            else:
                hf1,hf2, hart_steps = harts_one_line_algo(f,ret_steps=True)
                to_check.append(hf1)
                to_check.append(hf2)
                num_steps += hart_steps
        factors_so_far.extend(leftover_factors)
    if ret_steps:
        return factors_so_far, num_steps
    return factors_so_far

def check_harts_wrapper_correct(up_to=50):
    all_good = True
    for N in xrange(1,up_to):
        factors = harts_wrapper(N)
        f_prod = 1
        for f in factors:
            f_prod = f_prod *f
        if f_prod!=N:
            print factors,N, " --> oh no"
            all_good=False
    if all_good:
        print "all was good"

#print check_harts_wrapper_correct(100)
