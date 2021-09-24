def multiply(*args:int):
    numbers = [int(x) for x in args]
    num = 1
    for x in numbers:
        num = x * num
    return num