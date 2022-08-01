from primePy import primes
import math
from fractions import Fraction
while True:
   n = input('Enter some natural number ')
   if n == 'stop': break
   iter = input('Enter number of itrations ')
   try:
      v = int(n)
      s = int(iter)
      if s == 0:
          print(n)
      else:
          print()
          print('First number is ',n)
          print()
          m = 0
          while m < s:
              i = primes.factors(v)
              print('factors of ',v, 'are ', i) 
              j = []
              while len(i) > 0:
                  k = Fraction(1, i.pop())
                  j.append(k)
              a = int(v * sum(j))
              print('Relative complexity is ',sum(j), '=', float(sum(j)))
              print('Complexity is ',a)
              print()
              v = a
              m = m + 1 
   except:
      print('Bad input, try again') 
print('Have a good day')        
         
        

        
