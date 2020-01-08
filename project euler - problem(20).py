x = 1

for i in range(1,101):
    x *= i
    
x = str(x)
sum_ = 0

for i in x:
    sum_ += int(i)

print(sum_)
