bottles = int(input())
dishes = input()
detergent = bottles * 750
detergent_left = detergent
count = 1
dishes_count = 0
pots_count = 0
while dishes != "End":
    dishes_washed = int(dishes)
    if detergent_left >= 0:
        if count >= 3:
            count = 0
            detergent_left = detergent_left - (dishes_washed * 15)
            pots_count += dishes_washed
        else:
            detergent_left = detergent_left - (dishes_washed * 5)
            dishes_count += dishes_washed
    if detergent_left < 0:
        break
    count += 1
    dishes = input()
if detergent_left >= 0:
    print(f"Detergent was enough!"f"\n{dishes_count} dishes and {pots_count} pots were washed."f"\nLeftover detergent {detergent_left} ml.")
else:
    print(f"Not enough detergent, {abs(detergent_left)} ml. more necessary!")

