'''
Get data from a factory in Kazachstan.


'''

import requests
import simplejson as json

IP = '165.227.157.145'
PORT = '8080'
DIR = '/api/do_measurement'

def main():
    '''
    Main function.
    '''
    for x in range(-10, 11, 1):
        y = list()
        for rep in range(10):
            r = requests.get('http://'+IP+':'+PORT+DIR, params = {'x': x}).text
            # print(r)
            y.append(json.loads(r)['data']['y'])
        with open('data.txt', 'a') as f:
            print(str(x) + '\t' + '\t'.join(map(str,y)), file = f)

    print('ok')


if __name__ == '__main__':
    main()
