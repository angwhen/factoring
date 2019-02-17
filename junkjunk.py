import numpy as np
import matplotlib.pyplot as plt


N = 5
menMeans = np.array([-20, 35, 30, 35, 27])
womenMeans = [25, 32, 34, 20, 25]
transMeans = [25, 32, 34, 20, 28]
womenTop = [i+j for i,j in zip(menMeans,womenMeans)]
print womenTop
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width, bottom=menMeans, yerr=womenStd)
p3 = plt.bar(ind, transMeans, width, bottom=womenTop, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
print p1[0]
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()