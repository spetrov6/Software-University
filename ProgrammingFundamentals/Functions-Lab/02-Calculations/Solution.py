def calculus(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a // b
operator = input()
num1 = int(input())
num2 = int(input())
print(calculus(operator,num1,num2))
