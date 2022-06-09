
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:02:07 2022

@author: saqo2
"""

from primePy import primes
import math
from pylab import *
n = int(input('Enter some natural number '))
n1 = n
iter = int(input('Enter number of itrations '))
r = int(input('Enter range '))
def NC(n, iter):
    global xresult, yresult
    xresult = [0]
    yresult = [n]
    if(iter == 0):
        print(n)
    else:
        print()
        print('First number is ',n)
        print()
        m = 0
        while m < iter:
            i = primes.factors(n)
            print('factors of ',n,' are ', i)
            j = []
            while len(i) > 0:
                k = 1/i.pop()
                j.append(k)
            a = round(n * sum(j))
            print('Relative complexity is ',sum(j))
            print('Complexity is ',a)
            print()
            n = a
            m = m + 1
            xresult.append(m)
            yresult.append(a)
xlabel('Time')
ylabel('Value')            
for n in range(n1, n1+r, 1):
    NC(n, iter)
    plot(xresult, yresult, marker='o')        
show()    
    

        
         
        

        
