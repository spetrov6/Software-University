n = int(input())
l = int(input())

for one in range(1, n +1):
    for two in range(1, n + 1):
        for three in range(1, l + 1):
            three = chr(three + 96)
            for four in range(1, l + 1):
                four = chr(four + 96)
                for five in range(1, n + 1):
                  if one < five > two:
                      print(f"{one}{two}{three}{four}{five}", end=" ")