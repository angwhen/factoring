import math

def is_square(x):
    return x > 0 and int(math.sqrt(x)) == math.sqrt(x)

def gcd(A,B):
    A = int(A)
    B = int(B)
    while B != A and  B != 0:
        temp = B
        B = A % B
        A = temp
    return A

def harts_one_line_algo(N,L=-1):
    if L == -1:
        L = N
    for i in xrange(1,L):
        s = int(math.ceil(math.sqrt(N*i)))
        m = (s*s) % N
        if (is_square(m)):
            break
    t = math.sqrt(m)
    f1 = gcd(s-t,N) 
    f2 = N/f1
    return f1,f2

for N in xrange(2,30):
    print N,harts_one_line_algo(N)


