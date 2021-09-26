def min_max_sum(nums,negatives=[],positives=[]):
    if not nums:
        print(sum(negatives),sum(positives),sep="\n")
        if abs(sum(negatives)) > sum(positives):
            print(f"The negatives are stronger than the positives")
        else:
            print(f"The positives are stronger than the negatives")
        return
    if nums[0] < 0:
        negatives.append(nums[0])
    else:
        positives.append(nums[0])
    min_max_sum(nums[1:],negatives,positives)
numbers = [int(x) for x in input().split()]
min_max_sum(numbers)