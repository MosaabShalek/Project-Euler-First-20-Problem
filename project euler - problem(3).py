from prime_lib import *

n = 600851475143

primes = s_e(int(n**0.5))
while n != 1:
    for i in primes:
        if n%i == 0:
            n /= i
            print(i)
            break
        

