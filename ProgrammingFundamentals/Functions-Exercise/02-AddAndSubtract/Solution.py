def add_and_subtract(num1,num2,num3):
    def sum_numbers(a,b):
        return a + b
    def subtract(sum_for_subtract, c):
        return sum_for_subtract - c
    return subtract(sum_numbers(num1,num2),num3)
first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num,second_num,third_num))