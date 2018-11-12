import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

def get_residues(N):
    res_list = []
    for sq_rt in xrange(1,N-1):
        sq = sq_rt * sq_rt
        res = sq % N
        if res != 0:
            res_list.append(res)
    return res_list


def residues_heatmap(max_range):
    mat = np.zeros([max_range,max_range])
    for N in xrange(1,max_range+1):
        for res in get_residues(N):
            mat[res][N-1] += 1

    ax = sns.heatmap(mat)
    ax.invert_yaxis()
    ax.set_ylabel("N")
    ax.set_xlabel("residues")
    plt.show()
    return mat

mat = residues_heatmap(20)

#want to identify what those diagonals are
