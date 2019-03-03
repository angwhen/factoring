import math, random, time
import miller_rabin

def prime_gen1(digits, remove_prime_mults_up_to=1): #inclusive
    if remove_prime_mults_up_to > 7:
        raise ("Removing primes up to mults above 7 is not supported")
    
    start = time.time()
    primes_list = [1,2,3,5,7,11,13,17,19,23,29,31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    gen_steps = 0
    min_num, max_num = 10**(digits-1), 10**digits-1

    big, i = 1, -1
    while True:
        i+=1
        if primes_list[i] <= remove_prime_mults_up_to:
            big *= primes_list[i]
        else:
            break

    big_digits = int (math.floor(math.log(big)/math.log(10)))
    if big_digits >= digits:
        # if digits is same as big digits, will not be able to find some primes
        # if digits is less than big digits, will not be able to find any 
        return 0,0,0

    while True:
        curr_num = random.randint(min_num,max_num)
        
        # if not, is not a potential prime
        cont = True
        for p in xrange(0,i):
            gen_steps += 1
            if (curr_num-p) % big == 0:
                cont = False
        if cont:
            continue

        is_prime,mr_steps = miller_rabin.miller_rabin(curr_num,10)
        gen_steps += mr_steps
        if is_prime:
            end = time.time()
            return curr_num, gen_steps, end-start
        

# refernces: https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb
# https://math.stackexchange.com/questions/68473/fastest-prime-generating-algorithm