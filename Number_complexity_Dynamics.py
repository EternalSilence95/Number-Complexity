from primePy import primes
import math
n = int(input('Enter some natural number '))
iter = int(input('Enter number of itrations '))
if iter == 0:
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
        n = a
        m = m + 1
        
         
        

        

