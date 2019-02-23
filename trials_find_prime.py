import numpy as np
import prime_generators
import matplotlib.pyplot as plt 
import steps

n_list = []
gen_steps_list = []
gen_steps_std_list = []
num_iter = 10
for n in xrange(1,7):
    n_list.append(n)
    curr_gen_steps = []
    for i in xrange(0,num_iter):
        p,steps = prime_generators.prime_gen1(n)
        print n, p,steps
        curr_gen_steps.append(steps) #steps.get_gen_steps(steps)
    gen_steps_list.append(np.mean(curr_gen_steps))
    gen_steps_std_list.append(np.std(curr_gen_steps))
print n_list
print gen_steps_list
print gen_steps_std_list

ind, width = np.arange(len(gen_steps_list)), 0.35  
p1 = plt.bar(ind, gen_steps_list, width)

plt.ylabel('Steps')
plt.xlabel('N')
plt.title('Steps to Find Prime of N Digits')
plt.xticks(ind, n_list, rotation='vertical')
plt.yticks(np.arange(0, max(gen_steps_list)*1.2, 10))
   
plt.savefig("results/trials_to_find_prime_of_n_digits.png")
plt.close()

"""
ind, width = np.arange(len(gen_steps_list)), 0.35  
p1 = plt.bar(ind, gen_steps_std_list, width)

plt.ylabel('Steps')
plt.xlabel('N')
plt.title('STD of Steps to Find Prime of N Digits')
plt.xticks(ind, n_list, rotation='vertical')
plt.yticks(np.arange(0, max(gen_steps_std_list)*1.2, 10))
   
plt.savefig("results/std_trials_to_find_prime_of_n_digits.png")
"""