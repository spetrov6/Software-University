devisor = int(input())
bond = int(input())
max_num = 0
for n in range(1,bond + 1):
    if n % devisor == 0 and n > max_num:
        max_num = n
print(max_num)