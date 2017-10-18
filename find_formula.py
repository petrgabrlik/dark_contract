#!/usr/bin/env python3
'''
Process data and find unknown formula.

Entry task: https://github.com/kiwicom/mlweekend
Address example: http://165.227.157.145:8080/api/do_measurement?x=2
'''

import argparse
import numpy as np
import matplotlib.pyplot as plt


# Not my idea, solution by Gareth
# https://codegolf.stackexchange.com/questions/4707/outputting-ordinal-numbers-1st-2nd-3rd#answer-4712
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])


def count_missing(data):
    '''
    Function returns the count of missing values.
    '''
    nan = np.nan
    return np.sum(np.isnan(data[:,1:]))


def interpolate_missing(data):
    '''
    Linear interpolation of missing values.
    TODO: delete missing values which are at the edge of the interval
    '''
    nan = np.nan
    # Interpolate columns one by one
    for col in range(1, np.shape(data[:,1:])[1] + 1):
        x = data[np.isnan(data[:,col]),0]
        xp = data[~np.isnan(data[:,col]),0]
        fp = data[~np.isnan(data[:,col]),col]
        data[np.isnan(data[:,col]),col] = np.interp(x, xp, fp)


def filter_data(data):
    '''
    Average multiple measured data.
    '''
    # Copy x values and average y values
    num_of_rows = np.shape(data)[0]
    data_filt = np.zeros([num_of_rows,2])
    data_filt[:,0] = data[:,0]
    data_filt[:,1] = np.apply_along_axis( np.average, axis=1, arr=data[:,1:])
    return data_filt


def main(filename):
    '''
    The workflow.
    '''
    # Load data file
    # data = np.loadtxt(filename)
    data = np.genfromtxt(filename)

    # Count missing data
    missc = count_missing(data)
    if missc:
        print('Warning: {} ({:.1f}%) values missing'.format(missc, missc / data[:,1:].size * 100))

    # Interpolate missing data
    if missc:
        interpolate_missing(data)
        print('Missing data interpolated')

    # # Filter data
    data_filt = filter_data(data)

    # Plot input data
    plt.figure(1)
    plt.plot(data_filt[:,0], data_filt[:,1], '+b', markersize=10)
    plt.xlabel('x', fontweight='bold')
    plt.ylabel('y', fontweight='bold')
    plt.title('Filtered input data from {} file'.format(filename), fontweight='bold')
    # plt.show()
    plt.savefig('data_input.png', bbox_inches='tight')

    # Compare the data with function y=x^4
    p_x4 = np.poly1d([1, 0, 0, 0, 0])
    # Generate dense x array for plotting purposes
    x_dense = np.arange(np.ndarray.min(data[:,0]),
        np.ndarray.max(data[:,0]) + (np.ndarray.max(data[:,0]) - np.ndarray.min(data[:,0])) / 100,
        (np.ndarray.max(data[:,0]) - np.ndarray.min(data[:,0])) / 100)
    plt.figure(2)
    plt.plot(data_filt[:,0], data_filt[:,1], '+b',
        x_dense, p_x4(x_dense), '--g', markersize=10)
    plt.xlabel('x', fontweight='bold')
    plt.ylabel('y', fontweight='bold')
    plt.title('y=x^4 approximation', fontweight='bold')
    plt.legend(['Input data', 'y=x^4'])
    # plt.show()
    plt.savefig('data_input_x4.png', bbox_inches='tight')

    # Find best polynomial fit
    o = 4 # Polynomial order
    poly = np.polyfit(data_filt[:,0], data_filt[:,1], o)
    p = np.poly1d(poly)
    print('{} order polynomial function found by least squares fit:\n'.format(ordinal(o)), p)
    plt.figure(3)
    plt.plot(data_filt[:,0], data_filt[:,1], '+b',
        x_dense, p(x_dense), ':r', markersize=10)
    plt.xlabel('x', fontweight='bold')
    plt.ylabel('y', fontweight='bold')
    plt.title('{} order polynomial approximation'.format(ordinal(o)), fontweight='bold')
    plt.legend(['Input data', '{} order polynomial'.format(ordinal(o))])
    # plt.show()
    plt.savefig('data_input_p4.png', bbox_inches='tight')

    # Plot all together
    plt.figure(4)
    plt.plot(data_filt[:,0], data_filt[:,1],'+b',
        x_dense, p_x4(x_dense), '--g',
        x_dense, p(x_dense), ':r', markersize=10)
    plt.xlabel('x', fontweight='bold')
    plt.ylabel('y', fontweight='bold')
    plt.title('Comparison of approximations', fontweight='bold')
    plt.legend(['Input data', 'y=x^4', '{} order polynomial'.format(ordinal(o))])
    # plt.show()
    plt.savefig('data_input_x4_p4.png', bbox_inches='tight')

    plt.show()


if __name__ == '__main__':
    # Initialize and configure parser
    parser = argparse.ArgumentParser(description='App finds unknown formula.')
    parser.add_argument('data', type=str, help='File containing data, a required string argument')
    args = parser.parse_args()
    # Run main program
    main(args.data)
