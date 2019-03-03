import math, random, pickle, time
import prime_generators
import algos
from steps import AlgoSteps, Steps
import steps
import os.path
import matplotlib.pyplot as plt
import numpy as np


def step_algos(prime_digits,num_iter=10, graph_title = "", filename = "results/idk.png"):
    f_time_list_dict = {}
    h_time_list_dict = {}
    lf_time_list_dict = {}
    pr_time_list_dict = {}
    p1_time_list_dict = {}
    for prime_digits in xrange(3,7):
        f_time_list_dict[prime_digits] = []
        h_time_list_dict[prime_digits] = []
        lf_time_list_dict[prime_digits] = []
        pr_time_list_dict[prime_digits] = []
        p1_time_list_dict[prime_digits] = [] # bad variable names here, fix later TODO should be steps
        for i in xrange(0,num_iter):
            # Number Gen
            p1,_,_ = prime_generators.prime_gen1(prime_digits)
            p2,_,_ = prime_generators.prime_gen1(prime_digits)
            my_prime = p1*p2
            print "%d, %d" % (p1,p2)

            # Factoring (into 2, not whole)
           
            f_res1,f_res2,f_steps = algos.fermats_diff_of_squares(my_prime)
            f_time_list_dict[prime_digits].append(steps.get_gen_steps(f_steps))
 
            h_res1,h_res2,h_steps =  algos.harts_one_line(my_prime)
            h_time_list_dict[prime_digits].append(steps.get_gen_steps(h_steps))
  
            lf_res1,lf_res2,lf_steps = algos.lehmans_var_of_fermat(my_prime)
            lf_time_list_dict[prime_digits].append(steps.get_gen_steps(lf_steps))

            pr_res1,pr_res2,pr_steps = algos.pollards_rho(my_prime)
            pr_time_list_dict[prime_digits].append(steps.get_gen_steps(pr_steps))

            p1_res1,p1_res2,p1_steps = algos.pollards_pminus1(my_prime)
            p1_time_list_dict[prime_digits].append(steps.get_gen_steps(p1_steps))
        
    objects = ('Fermat', 'Hart', 'Lehmans', 'Poll Rho', 'Poll Minus')
    ind = np.arange(len(objects))
    av_times_3 = [np.mean(f_time_list_dict[3]),np.mean(h_time_list_dict[3]),np.mean(lf_time_list_dict[3]),np.mean(pr_time_list_dict[3]),np.mean(p1_time_list_dict[3])]
    av_times_4 = [np.mean(f_time_list_dict[4]),np.mean(h_time_list_dict[4]),np.mean(lf_time_list_dict[4]),np.mean(pr_time_list_dict[4]),np.mean(p1_time_list_dict[4])]
    av_times_5 = [np.mean(f_time_list_dict[5]),np.mean(h_time_list_dict[5]),np.mean(lf_time_list_dict[5]),np.mean(pr_time_list_dict[5]),np.mean(p1_time_list_dict[5])]
    av_times_6 = [np.mean(f_time_list_dict[6]),np.mean(h_time_list_dict[6]),np.mean(lf_time_list_dict[6]),np.mean(pr_time_list_dict[6]),np.mean(p1_time_list_dict[6])]
    width = 0.2

    p1 = plt.bar(ind, av_times_3, width)
    p2 = plt.bar(ind+width,av_times_4, width)
    p3 = plt.bar(ind+width*2, av_times_5, width)
    p4 =  plt.bar(ind+width*3, av_times_6, width)

    plt.xticks(ind, objects)
    plt.ylabel('Steps')
    plt.title(graph_title)
    plt.legend((p1[0], p2[0],p3[0],p4[0]), ("3","4","5","6"))

    plt.savefig(filename)

def time_algos(prime_digits,num_iter=10, graph_title = "", filename = "results/idk.png"):
    f_time_list_dict = {}
    h_time_list_dict = {}
    lf_time_list_dict = {}
    pr_time_list_dict = {}
    p1_time_list_dict = {}
    for prime_digits in xrange(3,7):
        f_time_list_dict[prime_digits] = []
        h_time_list_dict[prime_digits] = []
        lf_time_list_dict[prime_digits] = []
        pr_time_list_dict[prime_digits] = []
        p1_time_list_dict[prime_digits] = []
        for i in xrange(0,num_iter):
            # Number Gen
            p1,_,_ = prime_generators.prime_gen1(prime_digits)
            p2,_,_ = prime_generators.prime_gen1(prime_digits)
            my_prime = p1*p2
            print "%d, %d" % (p1,p2)

            # Factoring (into 2, not whole)
            start_time = time.time()
            f_res1,f_res2,f_steps = algos.fermats_diff_of_squares(my_prime)
            f_time_list_dict[prime_digits].append(time.time() - start_time)

            start_time = time.time()
            h_res1,h_res2,h_steps =  algos.harts_one_line(my_prime)
            h_time_list_dict[prime_digits].append(time.time() - start_time)

            start_time = time.time()
            lf_res1,lf_res2,lf_steps = algos.lehmans_var_of_fermat(my_prime)
            lf_time_list_dict[prime_digits].append(time.time() - start_time)

            start_time = time.time()
            pr_res1,pr_res2,pr_steps = algos.pollards_rho(my_prime)
            pr_time_list_dict[prime_digits].append(time.time() - start_time)

            start_time = time.time()
            p1_res1,p1_res2,p1_steps = algos.pollards_pminus1(my_prime)
            p1_time_list_dict[prime_digits].append(time.time() - start_time)
        
    objects = ('Fermat', 'Hart', 'Lehmans', 'Poll Rho', 'Poll Minus')
    ind = np.arange(len(objects))
    av_times_3 = [np.mean(f_time_list_dict[3]),np.mean(h_time_list_dict[3]),np.mean(lf_time_list_dict[3]),np.mean(pr_time_list_dict[3]),np.mean(p1_time_list_dict[3])]
    av_times_4 = [np.mean(f_time_list_dict[4]),np.mean(h_time_list_dict[4]),np.mean(lf_time_list_dict[4]),np.mean(pr_time_list_dict[4]),np.mean(p1_time_list_dict[4])]
    av_times_5 = [np.mean(f_time_list_dict[5]),np.mean(h_time_list_dict[5]),np.mean(lf_time_list_dict[5]),np.mean(pr_time_list_dict[5]),np.mean(p1_time_list_dict[5])]
    av_times_6 = [np.mean(f_time_list_dict[6]),np.mean(h_time_list_dict[6]),np.mean(lf_time_list_dict[6]),np.mean(pr_time_list_dict[6]),np.mean(p1_time_list_dict[6])]
    width = 0.2

    p1 = plt.bar(ind, av_times_3, width)
    p2 = plt.bar(ind+width,av_times_4, width)
    p3 = plt.bar(ind+width*2, av_times_5, width)
    p4 =  plt.bar(ind+width*3, av_times_6, width)

    plt.xticks(ind, objects)
    plt.ylabel('Time in Seconds')
    plt.title(graph_title)
    plt.legend((p1[0], p2[0],p3[0],p4[0]), ("3","4","5","6"))

    plt.savefig(filename)


  
step_algos(6,10,graph_title = "N Digit Prime Factor Comparison of Steps (10 Trials)", filename = "results/Ndigit_steps_comp.png")
