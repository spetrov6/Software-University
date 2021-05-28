n = int(input())
for first in range(1, 10):
    for second in range(1, 10):
        for third in range(1, 10):
            for fourth in range(1, 10):
                first_sum = first + second
                second_sum = third + fourth
                if first_sum == second_sum and n % first_sum == 0:
                    print(f"{first}{second}{third}{fourth}", end=" ")