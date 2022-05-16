# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:04:35 2022

@author: saqo2
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:02:07 2022

@author: saqo2
"""

from primePy import primes
import math
from pylab import *
n = int(input('Enter some natural number '))
iter = int(input('Enter number of itrations '))
xresult = []
yresult = []
def NC(n, iter):
    if(iter == 0):
        print(n)
    else:
        print('First number is ',n)
        m = 0
        while m < iter:
            i = primes.factors(n)
            print('factors are ', i)
            j = []
            while len(i) > 0:
                k = 1/i.pop()
                j.append(k)
            a = round(n * sum(j))
            print('Relative complexity is ',sum(j))
            print()
            print('Complexity is ',a)
            xresult.append(m)
            yresult.append(a)
            n = a
            m = m + 1
NC(n, iter) 
xlabel('time')    
ylabel('value')
plot(xresult, yresult)
show()        
    
    

        
         
        

        

