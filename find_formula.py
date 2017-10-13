'''
Process data and find unknown formula.

Entry task: https://github.com/kiwicom/mlweekend
Address example: http://165.227.157.145:8080/api/do_measurement?x=2
'''

import numpy as np
import matplotlib.pyplot as plt
import argparse


def main(filename):
    '''

    '''

    # Load data file
    data = np.loadtxt(filename)

    # Copy x values and averaged y values
    num_of_rows = np.shape(data)[0]
    data_filt = np.zeros([num_of_rows,2])
    data_filt[:,0] = data[:,0]
    data_filt[:,1] = np.apply_along_axis( np.average, axis=1, arr=data[:,1:])

    # print(data_filt)

    # poly = np.polyfit(data_filt[:,0], data_filt[:,1], 4)
    [poly, residuals, rank, singular_values, rcond] = np.polyfit(data_filt[:,0], data_filt[:,1], 4, full=True)
    print(residuals)
    p = np.poly1d(poly)

    print(poly)
    print(p)

    # Function y=x^4 for comparision
    p_x4 = np.poly1d([1, 0, 0, 0, 0])

    # Generate dense x array for plotting purposes
    x_dense = np.arange(np.ndarray.min(data[:,0]),
        np.ndarray.max(data[:,0]) + (np.ndarray.max(data[:,0]) - np.ndarray.min(data[:,0])) / 100,
        (np.ndarray.max(data[:,0]) - np.ndarray.min(data[:,0])) / 100)

    # Plot data
    plt.plot(data_filt[:,0], data_filt[:,1],'+r',
        x_dense, p(x_dense),'--b',
        x_dense, p_x4(x_dense), '--g')
    plt.xlabel(r'$\bf{x}$')
    plt.ylabel(r'$\bf{y}$')
    # plt.title(p)
    # plt.grid()
    plt.show()


if __name__ == '__main__':
    # Initialize and configure parser
    parser = argparse.ArgumentParser(description='App finds unknown formula.')
    parser.add_argument('data', type=str, help='File containing data, a required string argument')
    args = parser.parse_args()

    main(args.data)
