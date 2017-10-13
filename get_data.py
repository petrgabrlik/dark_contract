'''
Get data from the factory in Kazachstan.

Entry task: https://github.com/kiwicom/mlweekend
Address example: http://165.227.157.145:8080/api/do_measurement?x=2
'''

import requests
import simplejson as json
import os
import numpy as np
import argparse

IP = '165.227.157.145'
PORT = '8080'
DIR = '/api/do_measurement'

def main(limit_l, limit_h, step, rep):
    '''
    Main function.
    '''

    # Generate filename
    i = 0
    while os.path.exists("data{}.txt".format(i)):
        i += 1
    filename = "data{}.txt".format(i)

    steps = (limit_h - limit_l) / step
    c = 0

    print('Interval {},{}, step {}, rep {}'.format(limit_l, limit_h, step, rep))

    for x in np.arange(limit_l, limit_h, step):
        y = list()
        for i in range(rep):
            r = requests.get('http://'+IP+':'+PORT+DIR, params = {'x': x}).text
            # print(r)
            y.append(json.loads(r)['data']['y'])

        with open(filename, 'a') as f:
            print(str(x) + '\t' + '\t'.join(map(str,y)), file = f)

        # Pring percentage
        c += 1
        print('Downloading: {:2.0f} %'.format(c/steps*100), end='\r', flush=True)

    print('\nDownloading finished')
    print('Saved in {}'.format(filename))


if __name__ == '__main__':
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='App downloads data from the factory in Kazachstan.')
    # Required positional argument
    parser.add_argument('limit_l', type=float, help='Lower limit, a required float positional argument')
    parser.add_argument('limit_h', type=float, help='Upper limit, a required float positional argument')
    parser.add_argument('step', type=float, help='Iteration step, a required float positional argument')
    parser.add_argument('rep', type=int, help='The number of repetions, a required integer positional argument')
    # Parse
    args = parser.parse_args()

    main(args.limit_l, args.limit_h, args.step, args.rep)
