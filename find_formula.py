'''
Process data and find unknown formula.

Entry task: https://github.com/kiwicom/mlweekend
Address example: http://165.227.157.145:8080/api/do_measurement?x=2
'''

import numpy as np
import matplotlib

f = 'data0.txt'

for line in open(f):
    print(line.split('\t'))
