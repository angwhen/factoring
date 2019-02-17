import math
import random
import pickle
import prime_generators
import algos
from steps import AlgoSteps, Steps
import os.path

def time_algos(prime_digits,num_iter=10):
    # Loading Old Data if Any
    f_algo_steps,h_algo_steps,lf_algo_steps,pr_algo_steps,p1_algo_steps = AlgoSteps(),AlgoSteps(),AlgoSteps(),AlgoSteps(),AlgoSteps()
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


    for i in xrange(0,num_iter):
        # Number Gen
        p1,_ = prime_generators.prime_gen1(prime_digits)
        p2,_ = prime_generators.prime_gen1(prime_digits)
        my_prime = p1*p2
        print "%d, %d" % (p1,p2)

        # Factoring (into 2, not whole)
        f_res1,f_res2,f_steps = algos.fermats_diff_of_squares(my_prime)
        h_res1,h_res2,h_steps =  algos.harts_one_line(my_prime)
        lf_res1,lf_res2,lf_steps = algos.lehmans_var_of_fermat(my_prime)
        pr_res1,pr_res2,pr_steps = algos.pollards_rho(my_prime)
        p1_res1,p1_res2,p1_steps = algos.pollards_pminus1(my_prime)
        
        # Checking for Errors
        if f_res1 != p1 and f_res2 != p1:
            raise Exception("fermat problem, should get %d, %d, but got %d, %d"%(p1,p2,f_res1,f_res2))
        if h_res1 != p1 and h_res2 != p1:
            raise Exception("harts problem, should get %d, %d, but got %d, %d"%(p1,p2,h_res1,h_res2))
        if lf_res1 != p1 and lf_res2 != p1:
            raise Exception("lehmans var problem, should get %d, %d, but got %d, %d"%(p1,p2,lf_res1,lf_res2))
        if pr_res1 != p1 and pr_res2 != p1:
            raise Exception("pollards rho problem, should get %d, %d, but got %d, %d"%(p1,p2,pr_res1,pr_res2))
        if p1_res1 == None:
            p1_steps = Steps()
        elif p1_res1 != p1 and p1_res2 != p1:
            raise Exception("pollards pminus1, should get %d, %d, but got %d, %d"%(p1,p2,p1_res1,p1_res2))
        
        print str(f_steps)
        print pr_steps
        #Saving Steps
        f_algo_steps.add(my_prime,[p1,p2],f_steps)
        h_algo_steps.add(my_prime,[p1,p2],h_steps)
        lf_algo_steps.add(my_prime,[p1,p2],lf_steps)
        pr_algo_steps.add(my_prime,[p1,p2],pr_steps)
        p1_algo_steps.add(my_prime,[p1,p2],p1_steps)

    # Dumping New Data 
    pickle.dump( f_algo_steps, open("results/f_results.p", "wb" ) )
    pickle.dump( h_algo_steps, open("results/h_results.p", "wb" ) )
    pickle.dump( lf_algo_steps, open("results/lf_results.p", "wb" ) )
    pickle.dump( pr_algo_steps, open("results/pr_results.p", "wb" ) )
    pickle.dump( p1_algo_steps, open("results/p1_results.p", "wb" ) )
    
time_algos(2,10)