def device_facturial(n1,n2):
    factorial_num1 = 1
    factorial_num2 = 1
    for i in range(n1 - 1,0,-1):
        factorial_num1 += factorial_num1 * i
    for i in range(n2 - 1,0,-1):
        factorial_num2 += factorial_num2 * i
    print(f"{factorial_num1 / factorial_num2:.2f}")
device_facturial(int(input()),int(input()))