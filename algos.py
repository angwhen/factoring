import math
import random
from steps import Steps
import powering
import time

"""all methods return factors, num_steps, num_unfactored
num_unfactored of the last factors are not prime"""

def get_primes():
    p_list = []
    with open("P-10000.txt", "r") as f:
        for line in f:
            p_list.append(int(line.split(",")[1]))
    return p_list

def is_square(x):
    steps = Steps()
    steps.add_sqrt(x)
    return x >= 0 and int(math.sqrt(x)) == math.sqrt(x), steps

def gcd(A,B):
    A, B = int(A), int(B)
    steps = Steps()
    while B != A and  B != 0:
        temp = B
        steps.add_mod()
        B = A % B
        A = temp
    return A, steps

def trial_division(N,when_to_stop=None):
    primes_list = get_primes()
    m, pi, p = N, 0, 2
    steps = Steps()
    factors = []
    if when_to_stop == None:
        when_to_stop = math.sqrt(N)
        steps.add_sqrt(N)

    while (p <= when_to_stop):
        steps.add_mod()
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
    return factors, steps, num_unfactored

""" ******************************** INNERS ******************************** """

def fermats_diff_of_squares(N):
    if N%2 == 0:
        raise ValueError("Must be given odd N")
    steps = Steps()
    steps.add_sqrt(N)
    x = int(math.floor(math.sqrt(N)))
    t, r = 2*x+1, x*x - N
    isq, isq_steps = is_square(r)
    steps.append(isq_steps)
    while (not isq):
        r += t
        t += 2 
        isq, isq_steps = is_square(r)
        steps.append(isq_steps)
    x = (t-1)/2
    steps.add_sqrt(r)
    y = int(math.sqrt(r))
    return x-y, x+y, steps

def harts_one_line(N,L=-1):
    steps = Steps()
    if L == -1:
        L = N
    for i in xrange(1,L):
        steps.add_sqrt(N*i)
        s = int(math.ceil(math.sqrt(N*i)))
        steps.add_mod()
        m = (s*s) % N

        isq, isq_steps = is_square(m)
        steps.append(isq_steps)
        if (isq):
            break

    steps.add_sqrt(m)
    t = math.sqrt(m)
    f1, gcd_steps = gcd(s-t,N) 
    f2 = N/f1
    steps.append(gcd_steps)
    return f1, f2, steps

def lehmans_var_of_fermat(N):
    s3n = int(math.ceil(N**(1.0/3.0)))
    steps = Steps()
    for k in xrange(1,s3n+1):
        steps.add_sqrt(k*N)
        sk = 2.0 * math.sqrt(k*N)

        steps.add_exp(sk+N,1.0/6.0)
        steps.add_sqrt(k)
        for a in xrange(int(math.ceil(sk)),int(math.floor(sk+N**(1.0/6.0) / (4.0 * math.sqrt(k)))+1)):
            b = a*a - 4*k*N
        
            isq, isq_steps = is_square(b)
            steps.append(isq_steps)
            if isq:
                my_gcd, gcd_steps = gcd(a+math.sqrt(b),N)
                steps.append(gcd_steps)
                return my_gcd, N/my_gcd,steps
    raise Exception("should not get here ")

def pollards_rho(N,steps=None):
    if steps == None:
        steps = Steps()
    if N == 4:
        return 2, 2, steps

    b = random.randint(1,N-3)
    s = random.randint(0,N-1)
    A, B, g  = s,s,1
    while (g == 1):
        A = (A*A + b) % N 
        B = (((B*B+b)%N)*((B*B+b)%N)+b) % N
        g, g_steps = gcd(A-B,N)
        steps.append(g_steps)
    if g < N:
        return g, N/g, steps
    else: #continue until get a result
        return pollards_rho(N,steps)

def pollards_pminus1(N,B=None,steps=None):
    if steps == None:
        steps = Steps()
    if B == None:
        steps.add_cuberoot(N)
        B = math.pow(N,1.0/3.0)

    primes_list = get_primes()
    a, i = 2, 0
    a_set = set([])
    while True:
        pi = primes_list[i]
        if pi > B:
            break

        steps.add_log(B)
        steps.add_log(pi)
        e = int (math.floor(math.log(B)/math.log(pi)) )

        steps.add_exp(pi,e)
        f = pi**e

        steps.add_exp(a,f)
        steps.add_mod()
        a_hold = powering.power_mod(a,f,N) #(a**f) % N
        
        if a_hold == 0:
            break
        a = a_hold
        a_set.add(a)
        i += 1

    for a in a_set:
        g, g_steps = gcd(a-1,N)
        steps.append(g_steps)
        if 1 < g and g < N:
            return g, N/g, steps
    return None, None, steps

# TODO
def lehmers_factoring_method(N):
    return [N],0,1

""" ******************************** WRAPPERS ******************************** """

def fermats_diff_of_squares_prewrapper(N):
    steps = Steps()
    factors = []

    steps.add_mod()
    while N % 2 == 0:
        factors.append(2)
        N = N/2
        steps.add_mod()
    unfactored = [N]
    return factors, steps, unfactored

def harts_one_line_prewrapper(N):
    steps = Steps()
    factors, unfactored = [], [N]

    isq, isq_steps = is_square(N)
    steps.append(isq_steps)
    if not isq:
        steps.add_cuberoot(N)
        when_to_stop = math.pow(N,1.0/3.0)
        factors,tsteps,num_unfactored = trial_division(N, when_to_stop)
        steps.append(tsteps)
        unfactored = []
        if num_unfactored == 1:
            unfactored.append(factors[-1])
            factors = factors[:-1]

    return factors, steps, unfactored

def lehmans_var_of_fermat_prewrapper(N):
    steps = Steps()

    steps.add_cuberoot(N)
    s3n = int(math.ceil(N ** (1.0/3.0)))

    factors, tsteps, num_unfactored = trial_division(N,s3n)
    steps.append(tsteps)

    unfactored = []
    if num_unfactored == 1:
        unfactored.append(factors[-1])
        factors = factors[:-1]
    return factors, steps, unfactored

def pollards_pminus1_wrapper(N):
    steps = Steps()
    primes_list = get_primes()
    unfactored, factors = [N],[]
   
    while len(unfactored) > 0:
        n = unfactored.pop()
        if n in primes_list:
            factors.append(n)
        elif n == 1:
            continue
        else:
            steps.add_cuberoot(n)
            B = math.pow(n,1.0/3.0)

            f1,f2,hsteps = pollards_pminus1(n,B)
            steps.append(hsteps)
            if f1 == None: # p-1 wont work, trial division
                flist,tsteps,_ = trial_division(n)
                steps.append(tsteps)
                factors.extend(flist)
            else:
                unfactored.append(f1)
                unfactored.append(f2)

    return factors,steps,0

def wrapper(N, factoring_method):
    steps = Steps()

    if factoring_method == pollards_pminus1:
        return pollards_pminus1_wrapper(N)      

    # prewrappers recommended in joy of factoring
    if factoring_method == fermats_diff_of_squares:
        factors, psteps, unfactored = fermats_diff_of_squares_prewrapper(N)
    elif factoring_method == harts_one_line:
        factors, psteps, unfactored = harts_one_line_prewrapper(N)
    elif factoring_method == lehmans_var_of_fermat:
        factors, psteps, unfactored = lehmans_var_of_fermat_prewrapper(N)
    elif factoring_method == pollards_rho:
        factors, psteps, unfactored = [], Steps(), [N] #no prewrapper
    steps.append(psteps)

    primes_list = get_primes()
    while len(unfactored) > 0: 
        n = unfactored.pop()
        if n in primes_list:
            factors.append(n)
        elif n == 1:
            continue
        else:
            f1,f2,fsteps = factoring_method(n)
            steps.append(fsteps)
            unfactored.append(f1)
            unfactored.append(f2)

    return factors, steps, 0    
