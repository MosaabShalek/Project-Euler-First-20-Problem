sum_of_sq = sum([x**2 for x in range(1,101)])
sq_of_sum = sum([x for x in range(1,101)])**2
print(sq_of_sum - sum_of_sq)
