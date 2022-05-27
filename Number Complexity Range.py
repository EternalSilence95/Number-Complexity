# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:02:07 2022

@author: saqo2
"""

from primePy import primes
import math
from pylab import *
n = int(input('Enter some natural number '))
range = int(input('Enter the range '))
print()
l = n + range
xresult = []
yresult = []
def NC(n, range):
    while n < l:
        i = primes.factors(n)
        j = []
        while len(i) > 0:
            k = 1/i.pop()
            j.append(k)
        a = round(n * sum(j))
        print(n,' has Complexity ',a)
        xresult.append(n)
        yresult.append(a)
        n = n + 1
NC(n, range)
plot(xresult, yresult, marker='o')
show()     
    
    

        
         
        

        
