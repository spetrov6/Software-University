def expresion(nums,sum_result = 0,string_result=""):
    if not nums:
        print(f"{string_result}={sum_result}")
        return
    expresion(nums[1:],sum_result+nums[0],f"{string_result}+{nums[0]}")
    expresion(nums[1:],sum_result-nums[0],f"{string_result}-{nums[0]}")
numbers = [int(x) for x in input().split(", ")]
expresion(numbers)