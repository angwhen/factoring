import math
import random
import miller_rabin

def prime_gen1(digits):
    steps = 0
    min_num = 10**(digits-1)
    max_num = 10**digits-1
    while True:
        curr_num = random.randint(min_num,max_num)
        # check if is 6*n-1 or 6*n+1
        # if not, is not a potential prime
        steps += 1
        if (curr_num-1) % 6 != 0 and (curr_num+1) % 6 != 0:
            continue
        is_prime,mr_steps = miller_rabin.miller_rabin(curr_num,10)
        steps += mr_steps
        if is_prime:
            return curr_num, mr_steps
        

# refernces: https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb
# https://math.stackexchange.com/questions/68473/fastest-prime-generating-algorithm