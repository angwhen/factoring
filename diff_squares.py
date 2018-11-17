import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import math

# not efficient rn
def is_square(r):
    if r < 0:
        return False
    return int(math.sqrt(r)) == math.sqrt(r) 

def get_diff_squares_XY(N,ret_num_steps=False):
    """returns X and Y st X^2 - Y^2 = N"""
    if N % 2 == 0:
        raise ValueError("Must be given odd N")
    x = int(math.floor(math.sqrt(N)))
    t = 2*x+1
    r = x*x - N
    num_steps = 0
    while (not is_square(r)):
        r +=t
        t += 2
        num_steps +=1
        
    x = (t-1)/2
    y = int(math.sqrt(r))
    if ret_num_steps:
        return x,y,num_steps
    return x,y

def diff_squares_graph(upTo=10):
    X_list = []
    Y_list = []
    N_list = []
    num_steps_list = []
    for N in xrange(1,upTo,2): #only for odd
        x,y,num_steps = get_diff_squares_XY(N,True)
        X_list.append(x)
        Y_list.append(y)
        N_list.append(N)
        num_steps_list.append(num_steps)
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    plt.title("X and Ys such at X^2-Y^2 = N")
    ax = sns.scatterplot(N_list,X_list,palette="bright")
    ax = sns.scatterplot(N_list,Y_list,palette="deep")
    plt.xlabel("N")
    plt.ylabel("X and Ys")
    fig.savefig("diff_squares_XY_up_to_%d.png"%upTo)
    plt.show()
    
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    plt.title("Number of steps to find difference of squares representation")
    ax = sns.scatterplot(N_list,num_steps_list,palette="deep")
    plt.xlabel("N")
    plt.ylabel("Number of Steps")
    fig.savefig("diff_squares_steps_up_to_%d.png"%upTo)
    plt.show()

diff_squares_graph(1000)
