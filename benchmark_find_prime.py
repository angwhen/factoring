import numpy as np
import pickle
import prime_generators
import matplotlib.pyplot as plt 
import steps

def steps_and_time_between_short_circ_p():
    n_list = []
    gen_steps_list_dict = {}
    gen_time_list_dict = {}
    num_iter = 2
    for n in xrange(1,7):
        n_list.append(n)
        for short_circ_p in [1,3,5]:
            curr_gen_steps = []
            curr_gen_time = []
            for i in xrange(0,num_iter):
                p,steps,total_time = prime_generators.prime_gen1(n,short_circ_p)
                print n, p, steps, total_time
                curr_gen_steps.append(steps) 
                curr_gen_time.append(total_time)

            if short_circ_p not in gen_steps_list_dict:
                gen_steps_list_dict[short_circ_p] = []
            gen_steps_list_dict[short_circ_p].append(np.mean(curr_gen_steps))

            if short_circ_p not in gen_time_list_dict:
                gen_time_list_dict[short_circ_p] = []
            gen_time_list_dict[short_circ_p].append(np.mean(curr_gen_time))
        
    print n_list
    print gen_steps_list_dict
    print gen_time_list_dict


    ind, width = np.arange(len(n_list)), 0.15  
        
    p1 = plt.bar(ind, gen_steps_list_dict[1], width)
    p2 = plt.bar(ind+width, gen_steps_list_dict[3], width)
    p3 =  plt.bar(ind+width*2, gen_steps_list_dict[5], width)
    #p4 =  plt.bar(ind+width*3, gen_steps_list_dict[7], width)
    plt.ylabel('Steps')
    plt.xlabel('N')
    plt.title('Steps to Find Prime of N Digits')
    plt.xticks(ind, n_list, rotation='vertical')
    plt.yticks(np.arange(0, max(gen_steps_list_dict[5])*1.2, 25))
    plt.legend((p1[0], p2[0],p3[0]), ("1","3","5"))
    plt.savefig("results/steps_to_find_prime_of_n_digits.png")
    plt.close()


    p1 = plt.bar(ind, gen_time_list_dict[1], width)
    p2 = plt.bar(ind+width, gen_time_list_dict[3], width)
    p3 =  plt.bar(ind+width*2, gen_time_list_dict[5], width)
    #p4 =  plt.bar(ind+width*3, gen_time_list_dict[7], width)
    plt.ylabel('Time')
    plt.xlabel('N')
    plt.title('Time to Find Prime of N Digits')
    plt.xticks(ind, n_list, rotation='vertical')
    plt.yticks(np.arange(0, max(gen_time_list_dict[5])*1.2, 0.1))
    plt.legend((p1[0], p2[0],p3[0]), ("1","3","5"))
    plt.savefig("results/time_to_find_prime_of_n_digits.png")
    plt.close()

# graph of number numbers tested before finding prime per N 
def numbers_tested_graph():
    # will graph multiple bars for each N to show distribution
    return 0
    

#steps_and_time_between_short_circ_p
