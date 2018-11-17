import math
import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

def get_primes():
    p_list = []
    with open("P-10000.txt", "r") as f:
        for line in f:
            p_list.append(int(line.split(",")[1]))
    return p_list

def trial_division(N):
    primes_list = get_primes()
    m = N
    pi = 0
    factors = []
    p = 2
    while (p <= math.sqrt(N)):
        if m % p == 0:
            m = m/p
            factors.append(p)
        else:
            pi += 1
            p = primes_list[pi]
    if m != 1:
        factors.append(m)
    return factors

def trial_division_heatmap(max_range):
    mat = np.zeros([max_range,max_range])
    for N in xrange(0,max_range):
        for f in trial_division(N):
            mat[f][N] += 1
    fig,ax = plt.subplots(1,1)
    plt.title("factorings")
    ax = sns.heatmap(mat)
    ax.invert_yaxis()
    ax.set_ylabel("factors")
    ax.set_xlabel("N")
    fig.savefig("factorings_to_%d.png"%max_range)
    plt.show()
    return mat

trial_division_heatmap(30)
