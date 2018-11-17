import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import math

# not efficient rn
def is_square(r):
    if r < 0:
        return False
    return math.sqrt(r)*math.sqrt(r) == r 

def get_diff_squares_XY(N):
    """returns X and Y st X^2 - Y^2 = N"""
    x = int(math.floor(math.sqrt(N)))
    t = 2*x+1
    r = x*x - N
    while (not is_square(r)):
        r +=t
        t += 2
    x = (t-1)/2
    y = int(math.sqrt(r))
    return x,y

x,y = get_diff_squares_XY(527)
