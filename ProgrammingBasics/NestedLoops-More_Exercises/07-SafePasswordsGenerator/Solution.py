a = int(input())
b = int(input())
total_passwords = int(input())
password_count = 0
A = 35
B = 64
total = False
for x in range(1, a + 1):
    for y in range(1, b + 1):
        if password_count >= total_passwords:
            total = True
            break
        if A > 55:
            A = 35
        if B > 96:
            B = 64
        print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
        A += 1
        B += 1
        password_count += 1
    if total:
        break