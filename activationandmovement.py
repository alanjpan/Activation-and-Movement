# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 13:16:49 2018

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University

program framework for object activation and movement

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Activation and Movement [Computer software]. Github repository <https://github.com/alanjpan/Activation-and-Movement>

Note this software's license is GNU GPLv3.
"""

import math
import random

class Hub:
    def __init__(self, x, y):
        self.location = (x, y)
        self.activation = random.randrange(-100, 100, 1)

def distance(a, b):
    xdist = b[0] - a[0]
    ydist = b[1] - a[1]
    dist = math.sqrt(math.pow(xdist, 2) + math.pow(ydist, 2))
    return abs(round(dist, 3))

def energyexpense(a, b):
    expense = a - b
    return abs(round(expense, 3))

def main():
    a = Hub(random.randrange(0, 5), random.randrange(0, 5))
    b = Hub(random.randrange(5, 10), random.randrange(5, 10))
    c = Hub(random.randrange(10, 20), random.randrange(10, 20))

    travelrate = 1
    tr_ab = distance(a.location, b.location)
    tr_bc = distance(b.location, c.location)

    en_ab = energyexpense(a.activation, b.activation)
    en_bc = energyexpense(b.activation, c.activation)

    print('hub\tlocation\ttravel\tactivation')
    print('a\t' + str(a.location) + '\t\t' + str(tr_ab) + '\t' + str(a.activation))
    print('b\t' + str(b.location) + '\t\t' + str(tr_bc) + '\t' + str(b.activation))
    print('c\t' + str(c.location) + '\t0\t' + str(c.activation))

    dist_ab = round(travelrate * tr_ab, 3)
    dist_bc = round(travelrate * tr_bc, 3)

    print()
    print('a to b energy expended: ' + str(en_ab) + ' activation and ' + str(dist_ab) + ' movement')
    print('b to c energy expended: ' + str(en_bc) + ' activation and ' + str(dist_bc) + ' movement')
    total_ab = en_ab + dist_ab + en_bc + dist_bc
    print('total energy expended: ' + str(total_ab))

    tr_ac = distance(a.location, c.location)
    en_ac = energyexpense(a.activation, c.activation)
    dist_ac = travelrate * tr_ac

    print()
    print('a to c energy expended: ' + str(en_ac) + ' activation and ' + str(dist_ac) + ' movement')
    total_ac = en_ac + dist_ac
    print('total energy expended: ' + str(total_ac))
    
    if total_ac < total_ab:
        return 1
    else:
        return 0

count = 0
for i in range(10):
    print('\nTrial ' + str(i))
    count += main()
print('\n' + 'times ac < ab: ' + str(count) + '/10')