from prime_lib import *

primes = []
x = 1000
while len(primes) < 10001:
    primes = s_e(x)
    x *= 10
print(primes[10000])
