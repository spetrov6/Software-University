def recursive_power(num, power,number=0,counter=1):
    if counter == 1:
        number = num
    if power == counter:
        return number
    number = number * num
    return recursive_power(num, power, number,counter + 1)