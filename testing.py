import algos

success = False

for N in xrange(5,100):
    trial_factors,trial_steps,trial_left = algos.trial_division(N)
    my_factors,my_steps,my_left = algos.harts_one_line(N)
    my_factors.sort()
    if trial_factors != my_factors:
        print "FAILURE at N = ", N
        print trial_factors, my_factors
        break

if success:
    print "SUCCESS!"
