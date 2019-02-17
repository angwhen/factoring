import os, pickle
import numpy as np
import matplotlib.pyplot as plt
from steps import AlgoSteps

def graph_algo_steps(algo_steps,filename):
    sorted_zipped = sorted(zip(algo_steps.num_list,algo_steps.steps_list))
    num_list = [x for x,_ in sorted_zipped]
    steps_list = [x for _,x in sorted_zipped]

    num_mod_list = np.array([s.num_mod for s in steps_list])
    num_sqrt_list =  np.array([len(s.sqrt_list) for s in steps_list])
    num_cuberoot_list =  np.array([len(s.cuberoot_list) for s in steps_list])
    num_exp_list =  np.array([len(s.exp_list) for s in steps_list])
    num_log_list =  np.array([len(s.log_list) for s in steps_list])

    max_num = 10+max(num_mod_list) + max(num_sqrt_list)+max(num_cuberoot_list) + max(num_exp_list) + max(num_log_list)
    ind, width = np.arange(len(num_list)), 0.35  
    
    p1 = plt.bar(ind, num_mod_list, width)
    p2 = plt.bar(ind, num_sqrt_list, width, bottom = num_mod_list)
    p3 =  plt.bar(ind, num_cuberoot_list, width, bottom = num_mod_list+num_sqrt_list)
    p4 =  plt.bar(ind, num_exp_list, width, bottom = num_mod_list+num_sqrt_list+num_cuberoot_list)
    p5 =  plt.bar(ind, num_log_list, width, bottom = num_mod_list+num_sqrt_list+num_cuberoot_list+num_exp_list)
        
    plt.ylabel('Steps')
    plt.title('Steps of each type to factor numbers')
    plt.xticks(ind, num_list, rotation='vertical')
    plt.yticks(np.arange(0, max_num, 10))
    plt.legend((p1[0], p2[0],p3[0], p4[0], p5[0]), ('Mod', 'Sqrt','Cuberoot', 'Exp', 'Log'))
   
    plt.savefig(filename)

if os.path.isfile("results/f_results.p"):
    f_algo_steps = pickle.load( open( "results/f_results.p", "rb" ) )
if os.path.isfile("results/h_results.p"):
    h_algo_steps = pickle.load( open( "results/h_results.p", "rb" ) )
if os.path.isfile("results/lf_results.p"):
    lf_algo_steps = pickle.load( open( "results/lf_results.p", "rb" ) )
if os.path.isfile("results/pr_results.p"):
    pr_algo_steps = pickle.load( open( "results/pr_results.p", "rb" ) )
if os.path.isfile("results/p1_results.p"):
    p1_algo_steps = pickle.load( open( "results/p1_results.p", "rb" ) )

graph_algo_steps(f_algo_steps,"results/fermats_results.png")
graph_algo_steps(h_algo_steps,"results/harts_results.png")
graph_algo_steps(lf_algo_steps,"results/lehmans_var_results.png")
graph_algo_steps(pr_algo_steps,"results/pollards_rho_results.png")
graph_algo_steps(p1_algo_steps,"results/pollards_pminus1_results.png")