import math
import random
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

# steps is number of MOD operations
def gcd(A,B):
    A, B = int(A), int(B)
    steps = 0
    while B != A and  B != 0:
        steps +=1
        temp = B
        B = A % B
        A = temp
    return A, steps

# steps is # of MOD operations
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

def fermats_diff_of_squares_helper(N):
    if N%2 == 0:
        raise ValueError("Must be given odd N")
    x = int(math.floor(math.sqrt(N)))
    t = 2*x+1
    r = x*x - N
    steps = 0
    while (not is_square(r)):
        r += t
        t += 2 
        steps +=1
    x = (t-1)/2
    y = int(math.sqrt(r))
    return x-y, x+y, steps

# steps is # of checking for is_square
def fermats_diff_of_squares(N):
    primes_list = get_primes()
    factors = []
    steps = 0

    while N % 2 == 0:
        steps +=1
        factors.append(2)
        N = N/2
    
    to_check = []
    if N in primes_list:
        factors.append(N)
    elif N != 1:
        x,y,helper_steps = fermats_diff_of_squares_helper(N)
        to_check.append(x)
        to_check.append(y)
        steps += helper_steps
    while len(to_check) != 0:
        N = to_check.pop(0)
        if N in primes_list:
            factors.append(N)
        elif N != 1:
            x,y,helper_steps = fermats_diff_of_squares_helper(N)
            to_check.append(x)
            to_check.append(y)
            steps += helper_steps
    return factors,steps,0

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

# steps is # of MOD operations
def harts_one_line(N):
    # check if N sqare
    primes_list = get_primes()
    factors = [N]
    steps,num_unfactored = 0,1
    if not is_square(N):
        when_to_stop = math.pow(N,1.0/3.0)
        factors,steps,num_unfactored = trial_division(N, when_to_stop)
    if num_unfactored == 1: #not possible in trial division to have more unfactored
        N = factors[-1]
        factors = factors[:-1]
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

def lehmans_var_of_fermat_helper(N):
    s3n = int(math.ceil(N**(1.0/3.0)))
    steps = 0
    for k in xrange(1,s3n+1):
        sk = 2.0 * math.sqrt(k*N)
        for a in xrange(int(math.ceil(sk)),int(math.floor(sk+N**(1.0/6.0) / (4.0 * math.sqrt(k)))+1)):
            b = a*a - 4*k*N
            if is_square(b):
                my_gcd, gcd_steps = gcd(a+math.sqrt(b),N)
                steps += gcd_steps
                return my_gcd, N/my_gcd,steps
    return None,None,steps

# steps if # of MOD operations
#https://programmingpraxis.com/2017/08/22/lehmans-factoring-algorithm/
def lehmans_var_of_fermat(N):
    s3n = int(math.ceil(N ** (1.0/3.0)))
    factors, steps, num_unfactored = trial_division(N,s3n)
    unfactored = []
    if num_unfactored == 1:
        unfactored.append(factors[-1])
        factors = factors[:-1]
    primes_list = get_primes()

    while len(unfactored) > 0: 
        n = unfactored.pop()
        if n in primes_list:
            factors.append(n)
        elif n == 1:
            continue
        else:
            f1,f2,hsteps = lehmans_var_of_fermat_helper(n)
            unfactored.append(f1)
            unfactored.append(f2)
            steps += hsteps
    return factors, steps, 0

def lehmers_factoring_method(N):
    return [N],0,1

def pollards_rho_method_helper(N,steps=0):
    b = random.randint(1,N-3)
    s = random.randint(0,N-1)
    A, B, g  = s,s,1
    while (g == 1):
        A = A*A + b
        B = (B*B+b)*(B*B+b)+b
        g, g_steps = gcd(A-B,N)
        steps += g_steps
    if g < N:
        return g, N/g, steps
    else: #continue until get a result
        return pollards_rho_method_helper(N,steps)

#steps is # of MOD operations
def pollards_rho_method(N):
    unfactored = [N]
    steps, factors = 0, []
    primes_list = get_primes()
    while len(unfactored) > 0:
        n = unfactored.pop()
        if n in primes_list:
            factors.append(n)
        elif n == 1:
            continue
        elif n == 4: #too small to be handled by helper method
            factors.append(2)
            factors.append(2)
        else:
            f1,f2,psteps = pollards_rho_method_helper(n)
            unfactored.append(f1)
            unfactored.append(f2)
            steps += psteps
    return factors,steps,0

def pollards_pminus1_method_helper(N,B,steps=0):
    primes_list = get_primes()
    a = 2 
    i, steps = 0, 0
    a_set = set([])
    while True:
        pi = primes_list[i]
        if pi > B:
            break
        e = math.floor(math.log(B)/math.log(pi))
        f = math.pow(pi,e)
        a_hold = math.pow(a,f) % N
        steps +=1
        if a_hold == 0:
            break
        a = a_hold
        a_set.add(a)
        i += 1
    for a in a_set:
        g, g_steps = gcd(a-1,N)
        steps += g_steps
        if 1 < g and g < N:
            return g, N/g, steps
    return None, None, steps

# steps is # of MOD operations
def pollards_pminus1_method(N):
    # use B = N^1/3 as heuristc, did not say in book what to do
    primes_list = get_primes()
    unfactored, factors = [N],[]
    steps = 0
    while len(unfactored) > 0:
        n = unfactored.pop()
        if n in primes_list:
            factors.append(n)
        elif n == 1:
            continue
        else:
            B = math.pow(n,1.0/3.0)
            f1,f2,hsteps = pollards_pminus1_method_helper(n,B)
            steps += hsteps
            if f1 == None: # p-1 wont work, trial division
                flist,tsteps,_ = trial_division(n)
                steps += tsteps
                factors.extend(flist)
            else:
                unfactored.append(f1)
                unfactored.append(f2)

    return factors,steps,0

