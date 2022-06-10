# -*- coding: utf-8 -*-
"""
Created on Mon May 16 22:03:08 2022

@author: saqo2
"""

from primePy import primes
import math
from pylab import *
n = int(input('Enter some natural number '))
range = int(input('Enter the range '))
l = n + range
xresult = []
yresult = []
def NC(n, range):
    while n < l:
        i = primes.factors(n)
        print(n,' has factors ', i)
        j = []
        while len(i) > 0:
            k = 1/i.pop()
            j.append(k)
        print(n,' has relative Complexity ',sum(j))
        print()
        xresult.append(n)
        yresult.append(sum(j))
        n = n + 1
NC(n, range)
figure(dpi=1200)
plot(xresult, yresult, marker='o')
show()     
