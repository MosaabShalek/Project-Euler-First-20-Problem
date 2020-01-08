n = 1
for i in range(40, 0, -1):
    n *= i

b = 1
for i in range(20, 0, -1):
    b *= i

print(int(n/b**2))
