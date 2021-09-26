def check_numbers(type_of_numbers,numbers):
    sum_nums = 0
    for num in numbers:
        if type_of_numbers == "Odd":
            if num % 2 != 0:
                sum_nums += num
        else:
            if num % 2 == 0:
                sum_nums += num
    return sum_nums * len(numbers)
def main():
    numbers_type = input()                                               #Odd or even
    numbers_sequence = [int(x) for x in input().split()]
    sum_numbers = check_numbers(numbers_type,numbers_sequence)
    return sum_numbers
print(main())