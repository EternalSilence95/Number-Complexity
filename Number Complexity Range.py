# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:02:07 2022

@author: saqo2
"""

from primePy import primes
import math
from pylab import *
from fractions import Fraction
n = int(input('Enter some natural number '))
range = int(input('Enter the range '))
print()
l = n + range
xresult = []
yresult = []
def NC(n, range):
    while n < l:
        i = primes.factors(n)
        print(n,' has factors ',i)
        j = []
        while len(i) > 0:
            k = Fraction(1, i.pop())
            j.append(k)
        a = (n * sum(j))
        print(n,' has Complexity ',a)
        print()
        xresult.append(n)
        yresult.append(a)
        n = n + 1
NC(n, range)
figure(dpi=1200)
plot(xresult, yresult, marker='o')
show()     
    
    

        
         
        

        
