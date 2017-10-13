'''
Process data and find unknown formula.

Entry task: https://github.com/kiwicom/mlweekend
Address example: http://165.227.157.145:8080/api/do_measurement?x=2
'''

import sys
import numpy as np
import matplotlib.pyplot as plt


def main(filename):
    '''

    '''

    data = np.loadtxt(filename)

    num_of_rows = np.shape(data)[0]
    data_filt = np.zeros([num_of_rows,2])
    data_filt[:,0] = data[:,0]
    data_filt[:,1] = np.apply_along_axis( np.average, axis=1, arr=data[:,1:])

    print(data_filt)

    poly = np.polyfit(data_filt[:,0], data_filt[:,1], 4)
    p = np.poly1d(poly)

    print(poly)
    print(p)

    # y=x^4 function for comparision
    p_x4 = np.poly1d([1, 0, 0, 0, 0])

    plt.plot(data_filt[:,0], data_filt[:,1],'+r', np.arange(-10,10.1,0.1), p(np.arange(-10,10.1,0.1)),'--b', np.arange(-10,10.1,0.1), p_x4(np.arange(-10,10.1,0.1)), '--g')#, data_filt[:,0], data[:,1:], '+g')
    plt.xlabel(r'$\bf{x}$')
    plt.ylabel(r'$\bf{y}$')
    # plt.title(p)
    # plt.grid()
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Argument missing: pass data file as the argument")
