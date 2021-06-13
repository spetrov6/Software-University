places = int(input())
command = input()
count = 0
profit = 0
count_total = 0
places_left = places
while command != "Movie time!":
    count += int(command)
    count_total += count
    if count > places_left:
        print("The cinema is full.")
        break
    if count % 3 == 0:
        profit += (count * 5) - 5
    else:
        profit += count * 5
    places_left = places_left - count
    count = 0
    command = input()
if command == "Movie time!":
    print(f"There are {places - count_total} seats left in the cinema.")
print(f"Cinema income - {profit} lv.")

