starting_code = input()
ending_code = input()
for first in range(int(starting_code[0]),int(ending_code[0]) + 1):
    for second in range(int(starting_code[1]),int(ending_code[1]) + 1):
        for third in range(int(starting_code[2]),int(ending_code[2]) + 1):
            for four in range(int(starting_code[3]),int(ending_code[3]) + 1):
                if first % 2 != 0 and second % 2 != 0 and third % 2 != 0 and four % 2 != 0:
                    print(f"{first}{second}{third}{four}",end=" ")