import math, random, pickle, time
import prime_generators
import algos
from steps import AlgoSteps, Steps
import os.path
import matplotlib.pyplot as plt
import numpy as np

def time_algos(prime_digits,num_iter=10, graph_title = "", filename = "results/idk.png"):
    f_time_list = []
    h_time_list = []
    lf_time_list = []
    pr_time_list = []
    p1_time_list = []

    for i in xrange(0,num_iter):
        # Number Gen
        p1,_,_ = prime_generators.prime_gen1(prime_digits)
        p2,_,_ = prime_generators.prime_gen1(prime_digits)
        my_prime = p1*p2
        print "%d, %d" % (p1,p2)

        # Factoring (into 2, not whole)
        start_time = time.time()
        f_res1,f_res2,f_steps = algos.fermats_diff_of_squares(my_prime)
        f_time_list.append(time.time() - start_time)

        start_time = time.time()
        h_res1,h_res2,h_steps =  algos.harts_one_line(my_prime)
        h_time_list.append(time.time() - start_time)

        start_time = time.time()
        lf_res1,lf_res2,lf_steps = algos.lehmans_var_of_fermat(my_prime)
        lf_time_list.append(time.time() - start_time)

        start_time = time.time()
        pr_res1,pr_res2,pr_steps = algos.pollards_rho(my_prime)
        pr_time_list.append(time.time() - start_time)

        start_time = time.time()
        p1_res1,p1_res2,p1_steps = algos.pollards_pminus1(my_prime)
        p1_time_list.append(time.time() - start_time)
    
    objects = ('Fermat', 'Hart', 'Lehmans', 'Poll Rho', 'Poll Minus')
    y_pos = np.arange(len(objects))
    av_times = [np.mean(f_time_list),np.mean(h_time_list),np.mean(lf_time_list),np.mean(pr_time_list),np.mean(p1_time_list)]
 
    plt.bar(y_pos, av_times, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Time in Seconds')
    plt.title(graph_title)

    plt.savefig(filename)


  
time_algos(6,10,graph_title = "6 Digit Prime Factor Comparison of Runtime (10 Trials)", filename = "results/6digit_runtime_comp.png")