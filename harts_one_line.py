import math

def is_square(x):
    return x > 0 and int(math.sqrt(x)) == math.sqrt(x)

def gcd(A,B):
    return 1 #TODO

def harts_one_line_algo(N,L=-1):
    if L == -1:
        L = N
    for i in xrange(1,L):
        s = int(math.ceil(math.sqrt(N*i)))
        m = (s*s) % N
        if (is_square(m)):
            break
    t   = math.sqrt(m)
    return gcd(s-t,N) #a factor of N
for N in xrange(2,30):
    print N,harts_one_line_algo(N)
