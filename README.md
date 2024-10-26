# Number-Complexity

I generalized the idea of prime numbers, by defining a 'complexity' for natural numbers.

Complexity of n = n*(1/p1 + 1/p2 +...+1/pk), 
Relative Complexity of n = (1/p1 + 1/p2 +...+1/pk),
Where p1*p2*....*pk = n

By this definition all prime numbers have complexity 1
I also built a dynamical system by again applying complexity function on the output.
For some initial conditions applying complexity function again and again results in convergence to 1
for example 18 -> 21 -> 10 -> 7 -> 1 -> 1
and for some others it goes to infinity, for example 8 -> 12 -> 16 -> 32 -> 80 ->...

In future I hope to generalize this for at least rational and real numbers.
