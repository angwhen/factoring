import math

#returns a^b
def power(a,b):
    binary_b = bin(b)[2:]
    pows2_in_b = [] #ie if pow2_in_b = [0,2] then b = 2^0 + 2^2
    for i in xrange(len(binary_b)-1,-1,-1):
        if binary_b[i] == "1":
            pows2_in_b.append(len(binary_b)-i-1) 

    pows2a_dict = {}
    pows2a_dict[0] = a
    for i in xrange(1,len(binary_b)):
        pows2a_dict[i] = pows2a_dict[i-1] * pows2a_dict[i-1]
    
    res = 1
    for el in pows2_in_b:
        res *= pows2a_dict[el]
    return res

#returns (a^b) % c
def power_mod(a,b,c):
    binary_b = bin(b)[2:]
    pows2_in_b = [] #ie if pow2_in_b = [0,2] then b = 2^0 + 2^2
    for i in xrange(len(binary_b)-1,-1,-1):
        if binary_b[i] == "1":
            pows2_in_b.append(len(binary_b)-i-1) 

    pows2a_mod_dict = {}
    pows2a_mod_dict[0] = a % c
    for i in xrange(1,len(binary_b)):
        pows2a_mod_dict[i] = (pows2a_mod_dict[i-1] * pows2a_mod_dict[i-1]) % c
    
    res = 1
    for el in pows2_in_b:
        res *= pows2a_mod_dict[el]
        res = res % c
    return res

# ref: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation