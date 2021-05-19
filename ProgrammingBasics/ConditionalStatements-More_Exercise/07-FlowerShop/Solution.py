from math import floor,ceil
magnoli = int(input())
ziumbiuli = int(input())
rozi = int(input())
kaktusi = int(input())
gift = float(input())
profit_magnoli = magnoli * 3.25
profit_ziumbiuli = ziumbiuli * 4
profit_rozi = rozi * 3.50
profit_kaktusi = kaktusi * 8
profit = profit_rozi + profit_kaktusi + profit_magnoli + profit_ziumbiuli
tax = profit * 0.05
profit = profit - tax
if profit >= gift:
    print(f"She is left with {floor(profit - gift)} leva.")
else:
    print(f"She will have to borrow {ceil(gift - profit)} leva.")
