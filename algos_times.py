import math
import random
import prime_generators
import algos
# fermats_diff_of_squares_helper
# harts_one_line_helper
# lehmans_var_of_fermat_helper
# pollards_rho_method_helper
# pollards_pminus1_method_helper

def time_algos(prime_digits,num_iter=10):
    f= open("results.txt","a")
    for i in xrange(0,num_iter):
        p1,_ = prime_generators.prime_gen1(prime_digits)
        p2,_ = prime_generators.prime_gen1(prime_digits)
        print "%d, %d" % (p1,p2)
        f_res1,f_res2,f_steps = algos.fermats_diff_of_squares_helper(p1*p2)
        h_res1,h_res2,h_steps =  algos.harts_one_line_helper(p1*p2)
        lf_res1,lf_res2,lf_steps = algos.lehmans_var_of_fermat_helper(p1*p2)
        pr_res1,pr_res2,pr_steps = algos.pollards_rho_method_helper(p1*p2)
        p1_res1,p1_res2,p1_steps = algos.pollards_pminus1_method_helper(p1*p2)
        if f_res1 != p1 and f_res2 != p1:
            raise Exception("fermat problem, should get %d, %d, but got %d, %d"%(p1,p2,f_res1,f_res2))
        if h_res1 != p1 and h_res2 != p1:
            raise Exception("harts problem, should get %d, %d, but got %d, %d"%(p1,p2,h_res1,h_res2))
        if lf_res1 != p1 and lf_res2 != p1:
            raise Exception("lehmans var problem, should get %d, %d, but got %d, %d"%(p1,p2,lf_res1,lf_res2))
        if pr_res1 != p1 and pr_res2 != p1:
            raise Exception("pollards rho problem, should get %d, %d, but got %d, %d"%(p1,p2,pr_res1,pr_res2))
        if p1_res1 == None:
            p1_steps = -1
        elif p1_res1 != p1 and p1_res2 != p1:
            raise Exception("pollards pminus1, should get %d, %d, but got %d, %d"%(p1,p2,p1_res1,p1_res2))
        f.write("%d, %d, %d, %d, %d, %d, %d \n"%(p1,p2,f_steps,h_steps,lf_steps,pr_steps,p1_steps))
           
    
time_algos(2,2)