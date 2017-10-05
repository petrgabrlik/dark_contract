'''
Get data from a factory in Kazachstan.

Entry task: https://github.com/kiwicom/mlweekend
Address example: http://165.227.157.145:8080/api/do_measurement?x=2
'''

import requests
import simplejson as json
import os
import numpy as np

IP = '165.227.157.145'
PORT = '8080'
DIR = '/api/do_measurement'

def main():
    '''
    Main function.
    '''

    i = 0
    while os.path.exists("data{}.txt".format(i)):
        i += 1
    filename = "data{}.txt".format(i)

    limit_l = -0.5
    limit_h = 0.5
    step = 0.1
    steps = (limit_h - limit_l) / step
    c = 0

    for x in np.arange(limit_l, limit_h, step):
        y = list()
        for rep in range(10):
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
    main()
