import numpy as np

def get_residues(N):
    res_list = []
    for sq_rt in xrange(1,N-1):
        sq = sq_rt * sq_rt
        res = sq % N
        if res != 0 and res not in res_list:
            res_list.append(res)
    return sorted(res_list)


res_list_list = []
max_of_res = 0
max_range = 20
for N in xrange(1,max_range+1):
    res_list = get_residues(N)
    print N, res_list
    if len(res_list) != 0:
        max_of_res = max(max(res_list),max_of_res)
    res_list_list.append(res_list)

mat = np.zeros([max_range,max_of_res])
for N in xrange(1,max_range+1):
    for res in res_list_list[N-1]:
        mat[N-1][res-1] = 1

import matplotlib.pyplot as plt
plt.imshow(mat,cmap = 'hot',interpolation='nearest')
plt.show()
