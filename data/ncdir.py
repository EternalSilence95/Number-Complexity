
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:02:07 2022

@author: saqo2
"""

from primePy import primes
import math
from pylab import *
from fractions import Fraction
data1 = open('data1.txt', 'a')
while True:
   n = input('Enter some natural number ')
   if n == 'stop': break
   n1 = n
   i1 = input('Enter number of iterations ')
   r = input('Enter range ')
   # figure(dpi=1200)
   def NC(n, i1):
       n2 = int(n)
       i2 = int(i1)
       global xresult, yresult
       xresult = [0]
       yresult = [n]
       if(i2 == 0):
           print(n2, file = data1)
       else:
           print(file=data1)
           print('First number is ',n2, file=data1)
           print(file=data1)
           m = 0
           while m < i2:
               i = primes.factors(n2)
               print('factors of ',n2,' are ', i, file=data1)
               j = []
               while len(i) > 0:
                   k = Fraction(1, i.pop())
                   j.append(k)
               a = int(n2 * sum(j))
               print('Relative complexity is ',sum(j), '=', float(sum(j)), file=data1)
               print('Complexity is ',a, file=data1)
               print(file=data1)
               n2 = a
               m = m + 1
               xresult.append(m)
               yresult.append(a)
   xlabel('Time')
   ylabel('Value')   
   try:      
      for n in range(int(n1), int(n1)+int(r), 1):
          NC(n, i1)
          # plot(xresult, yresult, marker='o')
      # show()
   except:
      print('Bad input, try again')   
print('Have a good day')      
    
    

        
         
        

        
