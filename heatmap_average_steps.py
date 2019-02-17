import os, pickle
import numpy as np
import matplotlib.pyplot as plt
from steps import AlgoSteps, Steps
import seaborn

def get_gen_steps_list(algo_steps):
    steps_list = algo_steps.steps_list
    gen_steps_list = []
    for step in steps_list:
        gen_steps_list.append(get_gen_steps(step))
    return gen_steps_list

def get_gen_steps(steps):
    gen_steps = steps.num_mod + len(steps.exp_list) + len(steps.cuberoot_list)
    gen_steps += len(steps.sqrt_list) + len(steps.log_list)
    return gen_steps

# LOAD DATA
# algo1: 2 digit: [2,3,4,3,2]
#	     3 digit: [.....]	
def load_data_into_algo_digits_gensteps_dict(file_name_ending, num_digits, adgs_dict):
    f_algo_steps = pickle.load( open( "results/f_%s"%file_name_ending, "rb" ) )
    h_algo_steps = pickle.load( open( "results/h_%s"%file_name_ending, "rb" ) )
    lf_algo_steps = pickle.load( open( "results/lf_%s"%file_name_ending, "rb" ) )
    pr_algo_steps = pickle.load( open( "results/pr_%s"%file_name_ending, "rb" ) )
    p1_algo_steps = pickle.load( open( "results/p1_%s"%file_name_ending, "rb" ) )
    
    adgs_dict["f"][num_digits] = get_gen_steps_list(f_algo_steps)
    adgs_dict["h"][num_digits] = get_gen_steps_list(h_algo_steps)
    adgs_dict["lf"][num_digits] = get_gen_steps_list(lf_algo_steps)
    adgs_dict["pr"][num_digits] = get_gen_steps_list(pr_algo_steps)
    adgs_dict["p1"][num_digits] = get_gen_steps_list(p1_algo_steps)


def make_means_heatmap(adgs_dict,lowest_dig,highest_dig,filename):
    mat = np.zeros([5,highest_dig - lowest_dig +1])
    for i in xrange(lowest_dig, highest_dig+1):
        mat[0][i-lowest_dig] = np.mean(adgs_dict["f"][i])
        mat[1][i-lowest_dig] = np.mean(adgs_dict["h"][i])
        mat[2][i-lowest_dig] = np.mean(adgs_dict["lf"][i])
        mat[3][i-lowest_dig] = np.mean(adgs_dict["pr"][i])
        mat[4][i-lowest_dig] = np.mean(adgs_dict["p1"][i])
    print mat
    seaborn.heatmap(mat)
    plt.savefig(filename)

adgs_dict = {"f":{}, "h":{}, "lf":{}, "pr":{}, "p1":{}}
load_data_into_algo_digits_gensteps_dict("2digit.p",2, adgs_dict)
load_data_into_algo_digits_gensteps_dict("3digit.p",3, adgs_dict)
load_data_into_algo_digits_gensteps_dict("4digit.p",4, adgs_dict)

pickle.dump( adgs_dict, open("results/adgs_dict_2to4.p", "wb" ) )

make_means_heatmap(adgs_dict, 2, 4, "results/average_steps_2to4.png")