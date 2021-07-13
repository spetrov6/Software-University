nums = [int(i) for i in input().split(", ")]
result = []
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        result.append(i)
print(result)