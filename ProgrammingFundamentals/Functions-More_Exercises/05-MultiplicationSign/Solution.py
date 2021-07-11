def check_multiply(list_nums):
    negative = 0
    for i in list_nums:
        if i < 0:
            negative += 1
        elif i == 0:
            return "zero"
    if negative != 2 and negative != 0:
        return "negative"
    else:
        return "positive"
nums = [float(input()) for _ in range(3)]
print(check_multiply(nums))
