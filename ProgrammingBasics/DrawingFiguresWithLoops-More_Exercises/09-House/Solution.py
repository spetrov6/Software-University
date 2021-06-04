n = int(input())
stars_even = 2
stars_odd = 1
for row in range(1, n + 1):
    if row <= (n + 1) // 2:
        if n % 2 == 0:
            if stars_even < n:
                print("-" * (n // 2 - row) + "*" * stars_even + "-" * (n // 2 - row))
                stars_even += 2
            else:
                print("*" * stars_even)
        else:
            if stars_odd < n:
                print("-" * ((n // 2 + 1) - row) + "*" * stars_odd + "-" * ((n // 2 + 1) - row))
                stars_odd += 2
            else:
                print("*" * stars_odd)
    else:
        print("|" + "*" * (n - 2) + "|")
