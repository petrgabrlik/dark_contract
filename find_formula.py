'''
Process data and find unknown formula.

Entry task: https://github.com/kiwicom/mlweekend
Address example: http://165.227.157.145:8080/api/do_measurement?x=2
'''

import numpy as np
import matplotlib.pyplot as plt

f = 'data1.txt'

# for line in open(f):
#     print(line.split('\t'))

# plt.plotfile(f, delimiter='\t', cols=(0, 1))
# plt.show()

data = np.loadtxt(f)
# print(np.average(data[0][1:]))

# for i in np.nditer(data[:][1:]):
#     print(i)

# np.apply_along_axis( np.average, axis=1, arr=data[:,1:])
data_filt = np.zeros([20,2])
data_filt[:,0] = data[:,0]
data_filt[:,1] = np.apply_along_axis( np.average, axis=1, arr=data[:,1:])

print(data_filt)
plt.plot(data_filt[:,0], data_filt[:,1])
plt.show()
