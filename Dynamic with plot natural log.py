
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
i1 = int(input('Enter number of itrations '))
xresult = [0]
yresult = [math.log(n)]
def NC(n, i1):
    if(i1 == 0):
        print(n)
    else:
        print()
        print('First number is ',n)
        print('ln',n,' is ', math.log(n))
        print()
        m = 0
        while m < i1:
            i = primes.factors(n)
            print('factors of ', n,' are ' , i)
            j = []
            while len(i) > 0:
                k = Fraction(1, i.pop())
                j.append(k)
            a = int(n * sum(j))
            l = math.log(a)
            print('Relative complexity is ',sum(j), '=', float(sum(j)))
            print('Complexity is ',a)
            print('ln complexity is ', l)
            print()
            n = a
            m = m + 1
            xresult.append(m)
            yresult.append(l)
NC(n, i1)  
figure(dpi=1200)
xlabel('time')    
ylabel('ln value')  
plot(xresult, yresult, marker='o')
show()        
    
    

        
         
        

        
