command = input()
prime = 0
not_prime = 0
count = 0
while command != "stop":
    if int(command) < 0:
        print("Number is negative.")
        command = input()
        continue
    for i in range(1, int(command) + 1):
        if int(command) % i == 0:
            count += 1
    if count > 2:
        not_prime += int(command)
    else:
        prime += int(command)
    count = 0
    command = input()
print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {not_prime}")