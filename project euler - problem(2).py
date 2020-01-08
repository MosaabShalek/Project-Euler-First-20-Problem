x = [1,2]

while x[-1] < 4*10**6:
    x.append(x[-1] + x[-2])
    
print(sum(n for n in x if n%2==0))
