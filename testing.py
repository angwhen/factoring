import algos
import miller_rabin
import prime_generators
import random

#print algos.fermats_diff_of_squares_helper(27)
#print algos.fermats_diff_of_squares_helper(9)

#print algos.fermats_diff_of_squares(27)

def testing_factoring_algos():
        success = True
        for N in xrange(5,500):
                print N 
                trial_factors,trial_steps,trial_left = algos.trial_division(N)
                my_factors,my_steps,my_left = algos.wrapper(N,algos.pollards_rho)
                my_factors.sort()
                #print my_factors, trial_steps,my_steps
                if trial_factors != my_factors:
                        print "FAILURE at N = ", N
                        print trial_factors, my_factors
                        success = False
                        break

        if success:
                print "SUCCESS!"

def testing_primality_checkers():
        prime_list = algos.get_primes() 
        #goes up to around 100k in primes_list
        for i in xrange(1,50000):
                #print "testing %d" %i
                is_prime = i in prime_list
                mr_is_prime,steps = miller_rabin.miller_rabin(i,10)
                if is_prime != mr_is_prime:
                        print "was bad"
               
def testing_prime_gen():
        prime_list = algos.get_primes()
        for i in xrange(0,100): # 1000 iterations of tests
                print i,
                p,_ = prime_generators.prime_gen1(random.randint(3,5),7)
                print p
                if p not in prime_list:
                        print "FAILED"
                        return
        print "SUCESS"

testing_prime_gen()
                