one_lv = int(input())
two_lv = int(input())
five_lv = int(input())
total = int(input())
for one in range(one_lv + 1):
    for two in range(two_lv + 1):
        for five in range(five_lv + 1):
            check = (one * 1) + (two * 2) + (five * 5)
            if check  == total:
               print(f"{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {total} lv.")