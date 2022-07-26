from primePy import primes
import math
from fractions import Fraction
n = int(input('Enter some natural number '))
iter = int(input('Enter number of itrations '))
if iter == 0:
    print(n)
else:
    print()
    print('First number is ',n)
    print()
    m = 0
    while m < iter:
        i = primes.factors(n)
        print('factors are ', i) 
        j = []
        while len(i) > 0:
            k = Fraction(1, i.pop())
            j.append(k)
        a = round(n * sum(j))
        print('Relative complexity is ',sum(j), '=', float(sum(j)))
        print('Complexity is ',a)
        print()
        n = a
        m = m + 1
        
         
        

        

