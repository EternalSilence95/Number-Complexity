
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
xresult = [0]
yresult = [math.log(n)]
def NC(n, iter):
    if(iter == 0):
        print(n)
    else:
        print()
        print('First number is ',n)
        print('ln',n,' is ', math.log(n))
        print()
        m = 0
        while m < iter:
            i = primes.factors(n)
            print('factors of ', n,' are ' , i)
            j = []
            while len(i) > 0:
                k = 1/i.pop()
                j.append(k)
            a = round(n * sum(j))
            l = math.log(a)
            print('Relative complexity is ',sum(j))
            print('Complexity is ',a)
            print('ln complexity is ', l)
            print()
            n = a
            m = m + 1
            xresult.append(m)
            yresult.append(l)
NC(n, iter)  
figure(dpi=1200)
xlabel('time')    
ylabel('ln value')  
plot(xresult, yresult, marker='o')
show()        
    
    

        
         
        

        
