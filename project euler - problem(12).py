from prime_lib import prime_generator
from time import time

num1 = 1
adder = 1
mul = 1
t1 = time()

while mul < 500:
    adder += 1
    num1 += adder
    primes = prime_generator(int(num1**0.5))
    counter = 1
    mul = 1
    num2 = num1
    for i in primes:
        while num2%i == 0:
            num2 /= i
            counter += 1
        mul *= counter
        counter = 1
        if num2 == 1: break
    

t2 = time()
print(num1, t2-t1, mul)
        
