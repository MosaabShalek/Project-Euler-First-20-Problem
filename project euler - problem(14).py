import time
t1 = time.time()

chain_length = 0
max_chain_length = 0
for num in range(999999, 1, -1):
    answer = num
    while num != 1:
        if num%2 == 0: num /= 2
        else: num = 3*num +1
        chain_length += 1
    if chain_length > max_chain_length:
        max_chain_length = chain_length
        print(answer, chain_length)
    chain_length = 0
    
t2 = time.time()
print(t2 - t1)
    
    
