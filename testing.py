import algos

#print algos.fermats_diff_of_squares_helper(27)
#print algos.fermats_diff_of_squares_helper(9)

#print algos.fermats_diff_of_squares(27)

success = True
for N in xrange(5,100):
    print N 
    trial_factors,trial_steps,trial_left = algos.trial_division(N)
    my_factors,my_steps,my_left = algos.pollards_pminus1_method(N)
    my_factors.sort()
    print my_factors, trial_steps,my_steps
    if trial_factors != my_factors:
        print "FAILURE at N = ", N
        print trial_factors, my_factors
        success = False
        break

if success:
    print "SUCCESS!"
