import quad_residues #import get_residues
import math
import sys

def get_primes():
    p_list = []
    with open("P-10000.txt", "r") as f:
        for line in f:
            p_list.append(int(line.split(",")[1]))
    return p_list
def get_factors(N, with_quad = False):
    primes_list = get_primes()
    m = N
    pi = 0
    if with_quad:
        resN = quad_residues.get_residues(N)
        nonSquareResN = {}
        for r in resN:
            if math.sqrt(r) * math.sqrt(r) != r:
                nonSquareResN[r] = quad_residues.get_residues(r)
    factors = []
    p = 2
    while (p <= math.sqrt(N)):
        if m % p == 0:
            m = m/p
            factors.append(p)
        else:
            pi += 1
            p = primes_list[pi]
            bad = True
            while (with_quad and bad):
                bad = False
                for r in nonSquareResN.keys():
                    for rr in nonSquareResN[r]:
                        if p % r != rr:
                            bad = True
                if not bad:
                    break
                print "p: %d was not possible" %p
                pi += 1
                p = primes_list[pi]
    if m != 1:
        factors.append(m)
    return factors


print get_factors(int(sys.argv[1]),with_quad=True)

