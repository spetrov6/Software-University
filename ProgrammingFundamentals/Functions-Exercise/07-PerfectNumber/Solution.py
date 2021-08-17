def check_for_purfect_number(number):
    sum_of_number = sum([i for i in range(1,number) if number % i == 0])
    if sum_of_number == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."
print(check_for_purfect_number(int(input())))