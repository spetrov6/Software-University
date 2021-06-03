n = int(input())
for row in range(n + 1):
    for col in range(n - row):
        print(" ", end="")
    print("*" * row + " | " + "*" * row)
