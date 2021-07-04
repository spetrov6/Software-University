n = int(input())
negative_list = []
positive_list = []
sum_negative = 0
for i in range(n):
    num = int(input())
    if num < 0:
        negative_list.append(num)
        sum_negative += num
    else:
        positive_list.append(num)
print(f"{positive_list}\n{negative_list}")
print(f"Count of positives: {len(positive_list)}. Sum of negatives: {sum_negative}")