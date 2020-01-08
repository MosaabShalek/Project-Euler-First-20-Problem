nums = [i*j for i in range(100,1000) for j in range(100,1000)]
s_nums = [str(x) for x in nums]
nums2 = [int(i) for i in s_nums if i == i[::-1]]
answer = max(nums2)
print(answer)

